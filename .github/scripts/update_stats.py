"""
Daily stats updater for giga-meter-docs README.md.
Fetches live counts from the Giga Meter API and regenerates the country flag grid PNG.
Renders at 2x resolution (1440px wide) for crisp display on retina screens.

--- Release notes style guide ---
When updating the release hint block (between <!-- release-start --> and <!-- release-end -->),
write the body in this style:

  "Giga Meter can now [primary change] and [primary change], and [secondary change].
   The [app/software] also [supporting changes]."

Example:
  "Giga Meter can now measure internet speed more accurately and identify your location
   automatically, and the app is now available in Mongolian. The software also includes
   improvements to how it tracks usage and handles secure updates."

Rules:
- Lead with "Giga Meter can now" — user-benefit framing, not a changelog list
- Two sentences max: lead with the headline changes, close with supporting improvements
- Bold the header as: **Giga Meter X.Y.Z — YYYY-MM-DD**
- End with a link: [Full release notes →](GitHub release URL)
"""

import io
import math
import os
import re
import sys

import requests
from PIL import Image, ImageDraw, ImageFont

API_BASE = "https://meter.giga.global"

README_PATH = "README.md"
GRID_PATH = ".gitbook/assets/country-grid.png"

# Brand colours
GIGA_BLUE     = (39, 122, 255)   # #277AFF
GIGA_BLUE_MID = (26,  95, 212)   # placeholder flag tint
WHITE         = (255, 255, 255)

CANVAS_W = 1440


# ── Font loading ────────────────────────────────────────────────────────────

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
MANROPE_BOLD = os.path.join(SCRIPT_DIR, "Manrope-Bold.ttf")

def load_font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    candidates = []
    if bold:
        candidates += [
            MANROPE_BOLD,  # bundled — works on both macOS and Linux
            "/usr/share/fonts/truetype/open-sans/OpenSans-SemiBold.ttf",
            "/usr/share/fonts/truetype/open-sans/OpenSans-Bold.ttf",
            "/usr/share/fonts/truetype/lato/Lato-Bold.ttf",
            "/Library/Fonts/Arial Unicode.ttf",
        ]
    else:
        candidates += [
            MANROPE_BOLD,
            "/usr/share/fonts/truetype/open-sans/OpenSans-Regular.ttf",
            "/usr/share/fonts/truetype/lato/Lato-Regular.ttf",
            "/Library/Fonts/Arial Unicode.ttf",
        ]
    candidates += [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/System/Library/Fonts/Helvetica.ttc",
    ]
    for path in candidates:
        if os.path.exists(path):
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


# ── API helpers ─────────────────────────────────────────────────────────────

def fetch_metrics() -> dict:
    """Fetch aggregated stats from the public metrics endpoint."""
    resp = requests.get(f"{API_BASE}/api/v1/metrics", timeout=30)
    resp.raise_for_status()
    data = resp.json().get("data", {})
    print(f"  Metrics: {data.get('countries')} countries, {data.get('schools'):,} schools, {data.get('measurements'):,} measurements")
    return data


def fetch_countries() -> list[dict]:
    """Fetch all registered countries from the public /all endpoint for flag grid."""
    resp = requests.get(f"{API_BASE}/api/v1/dailycheckapp_countries/all", timeout=30)
    resp.raise_for_status()
    countries = resp.json().get("data", [])
    print(f"  Countries fetched for flag grid: {len(countries)}")
    return countries


# ── Flag fetching ────────────────────────────────────────────────────────────

def fetch_flag(iso2: str) -> Image.Image | None:
    url = f"https://flagcdn.com/w160/{iso2.lower()}.png"
    try:
        resp = requests.get(url, timeout=10)
        if resp.status_code == 200:
            return Image.open(io.BytesIO(resp.content)).convert("RGBA")
    except Exception:
        pass
    return None


def round_corners(img: Image.Image, radius: int) -> Image.Image:
    img = img.convert("RGBA")
    mask = Image.new("L", img.size, 0)
    ImageDraw.Draw(mask).rounded_rectangle(
        [(0, 0), (img.width - 1, img.height - 1)], radius=radius, fill=255
    )
    img.putalpha(mask)
    return img


# ── Country grid ─────────────────────────────────────────────────────────────

def generate_grid(countries: list[dict], countries_count: int = 0) -> Image.Image:
    countries_sorted = sorted(countries, key=lambda c: c.get("name", ""))
    n = len(countries_sorted)

    # Layout
    OUTER_H = 44          # left/right outer margin
    OUTER_V = 28          # top/bottom outer margin
    LEFT_COL_W = 260      # text column width
    COL_GAP = 32          # gap between text col and flags
    RIGHT_PAD = 32
    GRID_ROWS = 4
    CELL_GAP_H = 10
    CELL_GAP_V = 12
    CORNER_R = 5

    flags_x0 = OUTER_H + LEFT_COL_W + COL_GAP
    flag_area_w = CANVAS_W - flags_x0 - RIGHT_PAD
    grid_cols = math.ceil(n / GRID_ROWS)
    flag_w = (flag_area_w - CELL_GAP_H * (grid_cols - 1)) // grid_cols
    flag_h = flag_w * 2 // 3
    cell_h = flag_h + CELL_GAP_V
    total_h = OUTER_V * 2 + GRID_ROWS * cell_h

    img = Image.new("RGB", (CANVAS_W, total_h), GIGA_BLUE)
    draw = ImageDraw.Draw(img)

    # Left column: "Deployed in\nX countries" — use metrics count as authoritative label
    label = countries_count if countries_count else n
    line1, line2 = "Deployed in", f"{label} countries"
    font_size = 56
    font = load_font(font_size, bold=True)
    while font_size > 18:
        font = load_font(font_size, bold=True)
        w1 = draw.textbbox((0, 0), line1, font=font)[2]
        w2 = draw.textbbox((0, 0), line2, font=font)[2]
        if max(w1, w2) <= LEFT_COL_W:
            break
        font_size -= 2

    b1 = draw.textbbox((0, 0), line1, font=font)
    b2 = draw.textbbox((0, 0), line2, font=font)
    h1, h2 = b1[3] - b1[1], b2[3] - b2[1]
    line_gap = 6
    text_total_h = h1 + line_gap + h2
    text_y = (total_h - text_total_h) // 2

    draw.text((OUTER_H, text_y), line1, font=font, fill=WHITE)
    draw.text((OUTER_H, text_y + h1 + line_gap), line2, font=font, fill=WHITE)

    # Flags grid
    for i, country in enumerate(countries_sorted):
        col = i % grid_cols
        row = i // grid_cols
        x = flags_x0 + col * (flag_w + CELL_GAP_H)
        y = OUTER_V + row * cell_h

        flag = fetch_flag(country.get("code", ""))
        if flag:
            flag = round_corners(flag.resize((flag_w, flag_h), Image.LANCZOS), CORNER_R)
            img.paste(flag, (x, y), flag)
        else:
            draw.rounded_rectangle(
                [(x, y), (x + flag_w, y + flag_h)], radius=CORNER_R, fill=GIGA_BLUE_MID
            )

    return img


# ── README updater ───────────────────────────────────────────────────────────

def update_readme(countries_count: int, schools_count: int, measurements_count: int) -> None:
    with open(README_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    stats_block = (
        "<!-- stats-start -->\n"
        "{% columns %}\n"
        "{% column %}\n"
        f"#### {countries_count:,}\n\n"
        "Countries\n"
        "{% endcolumn %}\n\n"
        "{% column %}\n"
        f"#### {schools_count:,}\n\n"
        "Schools\n"
        "{% endcolumn %}\n\n"
        "{% column %}\n"
        f"#### {measurements_count:,}\n\n"
        "Measurements\n"
        "{% endcolumn %}\n"
        "{% endcolumns %}\n"
        "<!-- stats-end -->"
    )
    content = re.sub(
        r"<!-- stats-start -->.*?<!-- stats-end -->",
        stats_block, content, flags=re.DOTALL,
    )

    grid_block = (
        "<!-- country-grid-start -->\n"
        "![](docs/assets/country-grid.png)\n"
        "<!-- country-grid-end -->"
    )
    content = re.sub(
        r"<!-- country-grid-start -->.*?<!-- country-grid-end -->",
        grid_block, content, flags=re.DOTALL,
    )

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"  README updated: {countries_count} countries, {schools_count:,} schools, {measurements_count:,} measurements")


# ── Main ─────────────────────────────────────────────────────────────────────

def main() -> None:
    print("Fetching metrics...")
    metrics = fetch_metrics()
    countries_count = metrics.get("countries", 0)
    schools_count = metrics.get("schools", 0)
    measurements_count = metrics.get("measurements", 0)

    print("Fetching country list for flag grid...")
    countries = fetch_countries()

    print("Generating country grid image...")
    grid_img = generate_grid(countries, countries_count)
    os.makedirs(".gitbook/assets", exist_ok=True)
    grid_img.save(GRID_PATH, "PNG", optimize=True)
    print(f"  Saved: {GRID_PATH} ({grid_img.size[0]}×{grid_img.size[1]}px)")

    print("Updating README.md...")
    update_readme(countries_count, schools_count, measurements_count)

    print("Done.")


if __name__ == "__main__":
    main()
