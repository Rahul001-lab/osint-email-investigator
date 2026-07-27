# OSINT Email Investigator

A Python-based Open Source Intelligence (OSINT) tool designed to collect publicly available intelligence related to an email address.

> **Project Status:** 🚧 Under Development

---

## Project Goal

The objective of this project is **not to validate email addresses**, but to gather intelligence from publicly available sources that can assist during cybersecurity investigations and OSINT analysis.

Given an email address, the tool will collect relevant information such as domain details, DNS records, public profiles, breach information (where available), and other publicly accessible intelligence.

---

## Current Features

- ✅ Email parsing and basic input validation
- ✅ Domain information lookup
- ✅ WHOIS lookup
- ✅ DNS record enumeration
  - A Records
  - AAAA Records
  - MX Records
  - NS Records
  - TXT Records

---

## Planned OSINT Modules

### Core Intelligence
- 🔄 Email Parser
- 🔄 GitHub Intelligence
- 🔄 Reddit Intelligence
- 🔄 Gravatar Lookup
- 🔄 Search Engine Intelligence
- 🔄 Public Profile Discovery

### Infrastructure Intelligence
- 🔄 Domain Information
- ✅ WHOIS Lookup
- ✅ DNS Enumeration
- 🔄 Domain Age Analysis

### Breach Intelligence
- ⏳ Have I Been Pwned Integration (API Required)

### Reporting
- 🔄 Risk Assessment
- 🔄 Report Generator
- 🔄 Command Line Interface
- 🔄 GUI

---

## Project Structure

```
OSINT Email Investigator/
│
├── parser.py
├── domain_info.py
├── whois_info.py
├── dns_info.py
├── github_intel.py
├── reddit_intel.py
├── gravatar_intel.py
├── search_engine_intel.py
├── breach_checker.py
├── report_generator.py
├── main.py
└── README.md
```

---

## Technologies Used

- Python 3
- Requests
- python-whois
- dnspython
- JSON
- REST APIs

---

## Learning Objectives

This project is being developed to strengthen practical skills in:

- Python Programming
- Open Source Intelligence (OSINT)
- Networking Fundamentals
- DNS and WHOIS Analysis
- API Integration
- Cybersecurity Automation
- Modular Software Design
- Error Handling
- Report Generation

---

## Future Scope

- VirusTotal Integration
- Have I Been Pwned Integration
- Shodan Integration
- SecurityTrails Integration
- IntelligenceX Integration
- Multi-source OSINT Correlation
- PDF Report Generation
- Graphical User Interface (GUI)

---

## License

This project is intended for educational and cybersecurity learning purposes only.