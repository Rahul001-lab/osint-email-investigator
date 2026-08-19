# Email OSINT Investigator

Email OSINT Investigator is a Python-based OSINT tool designed to collect publicly available intelligence from an email address.

The tool extracts information from an email address and performs multiple OSINT lookups such as username intelligence, WHOIS information, DNS records, IP resolution, IP geolocation, Sherlock username discovery, and disposable email detection.

## Features

### Email Analysis

- Email format validation
- Username extraction
- Domain extraction
- TLD extraction
- Disposable email detection

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
- Background processing for long-running investigations

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
│   ├── disposable_email.py
│   ├── sherlock_lookup.py
│   └── email_detector.py
│
├── screenshots/
│
├── gui.py
├── main.py
├── README.md
├── LICENSE
├── requirements.txt
└── .gitignore

## Requirements

- Python 3.10 or newer
- Git
- Internet connection

## Installation

### 1. Clone the Repository

git clone https://github.com/Rahul001-lab/osint-email-investigator.git

Enter the project directory:

cd osint-email-investigator

### 2. Create a Virtual Environment

Windows:

python -m venv venv

Linux/macOS:

python3 -m venv venv

### 3. Activate the Virtual Environment

Windows:

venv\Scripts\activate

Linux/macOS:

source venv/bin/activate

### 4. Install Python Dependencies


pip install -r requirements.txt

### 5. Install Sherlock

Sherlock is required for username OSINT.

pip install sherlock-project

Verify the installation:


sherlock --version

You can also test Sherlock manually:

sherlock testusername

## Running the Application

After completing the installation:

python main.py

The Email OSINT Investigator GUI will open.

Enter an email address and click **Analyze** to begin the investigation.

## Investigation Flow

Email Address
      │
      ▼
Email Parser
      │
      ├──────────────► Username
      │                    │
      │                    ├──► GitHub
      │                    ├──► GitLab
      │                    └──► Sherlock
      │
      └──────────────► Domain
                           │
                           ├──► WHOIS
                           ├──► DNS Records
                           │
                           └──► IP Address
                                  │
                                  └──► Geolocation

## Sherlock Integration

The project uses Sherlock for username OSINT.

Sherlock searches the extracted username across multiple publicly available platforms and returns possible username matches.

The application runs Sherlock in the background so that long-running searches do not freeze the GUI.

Sherlock result files are disabled because the application captures the results directly and displays them in the GUI.

Sherlock results should be treated as possible matches and should not automatically be assumed to belong to the same individual.

## Disposable Email Detection

The tool checks whether the email domain matches known disposable email domains.

This feature uses a local list of disposable email domains and does not require an external API key.

## GitHub

The project is hosted on GitHub.

Clone the repository:

git clone https://github.com/Rahul001-lab/osint-email-investigator.git

To update an existing local copy:

git pull

## Development

To modify the project:

1. Clone the repository.
2. Create and activate a virtual environment.
3. Install the dependencies.
4. Make your changes.
5. Test the application.
6. Commit and push your changes.

Run the application during development with:

python main.py


## Screenshots


## Technologies Used

- Python
- CustomTkinter
- Requests
- Python-WHOIS
- DNSPython
- Sherlock Project
- Git
- GitHub

## Disclaimer

This project is intended for educational purposes, cybersecurity learning, and authorized OSINT investigations.

The tool attempts to collect publicly available information. Users are responsible for ensuring that their use of the tool complies with applicable laws, regulations, website terms of service, and privacy requirements.

Username matches from different platforms should not automatically be assumed to belong to the same individual.
