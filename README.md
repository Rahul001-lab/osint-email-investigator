# 📧 Email OSINT Investigator

A Python-based Email OSINT (Open Source Intelligence) tool that collects publicly available information related to an email address. The application features a modern GUI built with CustomTkinter and a modular architecture for easy maintenance and future expansion.

---

## ✨ Features

- Email validation
- Username extraction
- Domain extraction
- Top-Level Domain (TLD) extraction
- GitHub username lookup
- WHOIS lookup
- DNS record lookup
- IP address resolution
- Modern desktop GUI
- Modular architecture

---

## 📂 Project Structure

```
Email-OSINT-Investigator/
│
├── main.py
├── gui.py
├── README.md
├── requirements.txt
│
├── modules/
│   ├── __init__.py
│   ├── email_detector.py
│   ├── parser.py
│   ├── github_intel.py
│   ├── whois_lookup.py
│   ├── dns_info.py
│   └── dns_lookup.py
│
├── screenshots/
│
└── .gitignore
```

---

## 🛠 Technologies Used

- Python 3
- CustomTkinter
- Requests
- Python-WHOIS
- dnspython
- Regular Expressions (re)
- Socket Programming

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/email-osint-investigator.git
```

Move into the project folder

```bash
cd email-osint-investigator
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python main.py
```

---

## 🔍 Information Collected

### Email Information

- Email Address
- Username
- Domain
- Top-Level Domain (TLD)

### GitHub Intelligence

- Username
- Name
- Bio
- Company
- Location
- Public Repositories
- Followers
- Following
- Profile URL

### WHOIS Information

- Registrar
- Creation Date
- Expiration Date
- Name Servers

### DNS Records

- A Records
- AAAA Records
- MX Records
- NS Records
- TXT Records

### Domain Resolution

- Public IP Address

---

## 🏗 Architecture

```
                User
                  │
                  ▼
              main.py
                  │
                  ▼
               gui.py
                  │
                  ▼
     modules/email_detector.py
                  │
      ┌───────────┼──────────────┐
      ▼           ▼              ▼
 parser.py   github_intel.py   whois_lookup.py
                  │
                  ▼
             dns_info.py
                  │
                  ▼
             dns_lookup.py
```

---

## 🚀 Future Improvements

- Gravatar Lookup
- Social Media Search
- Data Breach Detection
- Email Reputation Check
- Domain Reputation Analysis
- Geolocation Lookup
- PDF Report Export
- Risk Score Calculation
- Background Threading
- Dark/Light Theme Support

---

## 📸 Screenshots

Screenshots will be added after project completion.

---

## 👨‍💻 Author

**Rahul Tewatia**

Cybersecurity Enthusiast | Python Developer | Networking Learner

---

## 📄 License

This project is intended for educational and ethical OSINT purposes only.