# Email OSINT Investigator

Email OSINT Investigator is a Python-based OSINT tool designed to collect publicly available intelligence from an email address.

The tool extracts information from an email address and performs multiple lookups such as username intelligence, WHOIS information, DNS records, IP resolution, and IP geolocation.

## Features

### Email Analysis
- Email format validation
- Username extraction
- Domain extraction
- TLD extraction

### Username Intelligence
- GitHub username lookup
- GitLab username lookup
- Sherlock username search across multiple platforms

### Domain Intelligence
- WHOIS information
- Registrar information
- Domain creation date
- Domain expiration date
- Name servers

### DNS Intelligence
- A records
- AAAA records
- MX records
- NS records
- TXT records

### IP Intelligence
- Domain to IP resolution
- IP geolocation
- Country
- Region
- City
- ZIP code
- Latitude
- Longitude
- Timezone
- ISP

### GUI
- Dark themed interface
- Email input
- Analyze button
- Clear button
- Organized investigation results
- Investigation status display

## Project Structure

```text
osint-email-investigator/
│
├── modules/
│   ├── parser.py
│   ├── github_intel.py
│   ├── gitlab_lookup.py
│   ├── whois_lookup.py
│   ├── dns_info.py
│   ├── dns_lookup.py
│   ├── geolocation.py
│   ├── sherlock_lookup.py
│   └── email_detector.py
│
├── gui.py
├── main.py
├── README.md
└── requirements.txt