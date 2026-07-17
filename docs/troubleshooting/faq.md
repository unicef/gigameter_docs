# FAQ

1. [How can I view my school's data?](faq.md#how-can-i-view-my-schools-data)
2. [What data does Giga Meter transmit to Giga?](faq.md#what-data-does-giga-meter-transmit-to-giga)
3. [Will Giga have access to any other information on my computer?](faq.md#will-giga-have-access-to-any-other-information-on-my-computer)
4. [Who will have access to my school connectivity data?](faq.md#who-will-have-access-to-my-school-connectivity-data)
5. [What is a School ID?](faq.md#what-is-a-school-id)
6. [How do I find my School ID?](faq.md#how-do-i-find-my-school-id)
7. [Can I close the application?](faq.md#can-i-close-the-application)
8. [How do I update the application?](faq.md#how-do-i-update-the-application)
9. [When do speed tests run?](faq.md#when-do-speed-tests-run)
10. [Where can I see past measurement results?](faq.md#where-can-i-see-past-measurement-results)
11. [Can I change my school ID?](faq.md#can-i-change-my-school-id)
12. [Can I install Giga Meter on more than one computer?](faq.md#can-i-install-giga-meter-on-more-than-one-computer)
13. [What kind of data does Giga Meter access?](faq.md#what-kind-of-data-does-giga-meter-access)
14. [How does Giga Meter help improve internet access?](faq.md#how-does-giga-meter-help-improve-internet-access)

***

#### How can I view my school's data?

You can view results in two ways:

1. **In the app** - the last 10 successful measurements are shown on the app's Data page.
2. **On Giga Maps** - visit [maps.giga.global/map](https://maps.giga.global/map), type your school name or ID in the left-hand panel, and select it to view results over time.

The dot next to each school is colour-coded by connectivity level:

**Green** - Good connectivity. The school meets or exceeds the selected benchmark.

<figure><img src="https://448102781-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FnO4TCnw5Pvr77OIRKx3h%2Fuploads%2Fgit-blob-d0311408be9a66ae4b6f73b899bbd6aae3d4b2e3%2Fmaps-green-good.png?alt=media" alt="Celetyuma Primary School - 51.99 Mbps, green dot"><figcaption></figcaption></figure>

**Yellow** - Moderate connectivity. The school is below the benchmark but has a working connection.

<figure><img src="https://448102781-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FnO4TCnw5Pvr77OIRKx3h%2Fuploads%2Fgit-blob-4c652b3f40a8c7d0b03672c844510115100b7a52%2Fmaps-yellow-moderate.png?alt=media" alt="Lonwabo Senior Secondary School - 7.87 Mbps, yellow dot"><figcaption></figcaption></figure>

**Red** - Slow connectivity. The school is significantly below the benchmark.

<figure><img src="https://448102781-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FnO4TCnw5Pvr77OIRKx3h%2Fuploads%2Fgit-blob-76e01b1f258697ad2ddb97e08fd0e34b78cdefaf%2Fmaps-red-slow.png?alt=media" alt="Embekweni Junior Primary School - 0.8 Mbps, red dot"><figcaption></figcaption></figure>

A **blue** dot means no recent data has been received; the device may be off or the app may need reinstalling.

After selecting your school, copy the URL from your browser's address bar. You can bookmark it for direct access any time.

***

#### What data does Giga Meter transmit to Giga?

The app transmits only network performance data. It does not collect browsing history, search activity, or personal files.

| Field                    | Example                | What it is                                                                                             |
| ------------------------ | ---------------------- | ------------------------------------------------------------------------------------------------------ |
| **Download speed**       | 10 Mbps                | Rate at which data travels from an M-Lab server to the device (NDT7 protocol, 10-second test)          |
| **Upload speed**         | 5.7 Mbps               | Rate at which data travels from the device to an M-Lab server (NDT7 protocol, 10-second test)          |
| **Latency**              | 3 ms                   | Round-trip time for a small packet to travel from the device to a server and back                      |
| **Packet loss**          | 0.5%                   | Percentage of data packets sent that never arrive at their destination                                 |
| **Uptime**               | 99%                    | Proportion of school hours (8am-8pm) during which the connection is confirmed reachable, from pings    |
| **ISP / ASN**            | AS8193 Uzbektelekom    | The internet service provider and its Autonomous System Number, a globally assigned network identifier |
| **IP address**           | 84.54.71.31            | The public IP address assigned to the school's connection at the time of measurement                   |
| **Test server location** | Chennai, IN            | Geographic location of the M-Lab measurement server used in the speed test                             |
| **Device type**          | windows                | Operating system running the measurement application                                                   |
| **Network name (SSID)**  | MERCUSYS\_43A4         | Name of the Wi-Fi network the device is connected to at the time of the test                           |
| **Wi-Fi standard**       | 802.11n                | Wi-Fi protocol version in use (802.11n = Wi-Fi 4, 802.11ac = Wi-Fi 5, 802.11ax = Wi-Fi 6)              |
| **Wi-Fi channel**        | 10                     | Radio frequency channel the router is broadcasting on                                                  |
| **Wi-Fi signal level**   | -70.5 dBm              | Signal strength received by the device. Closer to 0 is stronger; below -80 dBm is poor                 |
| **Wi-Fi transmit rate**  | 300 Mbps               | Speed at which the device's wireless adapter sends data to the router (the wireless link rate)         |
| **Wi-Fi adapter model**  | Intel Wireless-AC 9560 | Hardware model of the Wi-Fi adapter inside the measurement device                                      |

***

#### Will Giga have access to any other information on my computer?

No. The application does not access any data stored on your computer other than the network measurements described above.

***

#### Who will have access to my school connectivity data?

Upload speed, download speed, latency, and ping results are shared publicly, together with information about the registered school. This data is displayed on Giga Maps. No personal data is shared.

***

#### What is a School ID?

A School ID is a unique identifier for your school, provided by the government. Formats vary by country, but it typically looks like `BR12345` or `12345678`.

***

#### How do I find my School ID?

Ask your school administrator or IT department. The school ID is the number used in your national school registration system.

***

#### Can I close the application?

Yes. Clicking the close button closes the window, but the app continues running in the background and keeps reporting your connectivity status.

***

#### How do I update the application?

When a new version is available, a notification pop-up appears; click **Restart** to update. You can also visit [meter.giga.global](https://meter.giga.global/) at any time to download and install the latest version.

***

#### When do speed tests run?

Up to four speed tests run per day:

* First test: within 15 minutes of the device being powered on
* Remaining tests: within the time slots 8am-12pm, 12pm-4pm, and 4pm-8pm (local time)

Ping tests run every 15 minutes between 8am and 8pm local time.

You can also trigger a manual test at any time.

***

#### Where can I see past measurement results?

* **In the app:** the last 10 successful tests are shown on the Data page.
* **On Giga Maps:** daily averages are published to [maps.giga.global](https://maps.giga.global/). Find your school to see how its connectivity compares over time.

***

#### Can I change my school ID?

If you registered with the wrong school ID, you can unregister and re-register. See [Troubleshooting - Registered with the wrong school ID](troubleshooting.md).

***

#### Can I install Giga Meter on more than one computer?

Yes, and we encourage it. If multiple machines report data from the same school, measurements are more reliable.

***

#### What kind of data does Giga Meter access?

Only the system and network information needed to measure internet quality: connection speed, availability, network details, and device type. It does not access personal files, browsing history, or content.

***

#### How does Giga Meter help improve internet access?

Giga Meter does not fix internet connections directly, but it makes problems visible. The data helps governments and providers identify and prioritise improvements where they are needed most.

***

For further guidance, visit [meter.giga.global](https://meter.giga.global/) or the help section in the app.
