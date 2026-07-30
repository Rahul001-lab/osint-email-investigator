import customtkinter as ctk
from tkinter import END

from parser import parse_email
from github_intel import github_lookup
from whois_info import whois_lookup
from dns_info import get_dns_records
from domain_info import get_ip


class EmailOSINTGUI:

    def __init__(self):

        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("blue")

        self.root = ctk.CTk()

        self.root.title("Email OSINT Investigator")
        self.root.geometry("900x700")

        self.title = ctk.CTkLabel(
            self.root,
            text="Email OSINT Investigator",
            font=("Arial", 28, "bold")
        )

        self.title.pack(pady=20)

        self.input_frame = ctk.CTkFrame(self.root)

        self.input_frame.pack(fill="x", padx=20)

        self.email_entry = ctk.CTkEntry(
            self.input_frame,
            placeholder_text="Enter Email Address",
            width=500
        )

        self.email_entry.pack(side="left", padx=10, pady=15)

        self.analyze_button = ctk.CTkButton(
            self.input_frame,
            text="Analyze",
            command=self.analyze_email
        )

        self.analyze_button.pack(side="left", padx=10)

        self.clear_button = ctk.CTkButton(
            self.input_frame,
            text="Clear",
            command=self.clear_results
        )

        self.clear_button.pack(side="left")

        self.progress = ctk.CTkProgressBar(self.root)

        self.progress.pack(fill="x", padx=20, pady=15)

        self.progress.set(0)

        self.status = ctk.CTkLabel(
            self.root,
            text="Status : Waiting..."
        )

        self.status.pack()

        self.results = ctk.CTkTextbox(
            self.root,
            width=850,
            height=450,
            font=("Consolas", 13)
        )

        self.results.pack(padx=20, pady=20)

    def analyze_email(self):

        email = self.email_entry.get().strip()

        if not email:
            self.status.configure(text="Status : Please enter an email address.")
            return

        self.results.delete("1.0", END)

        self.progress.set(0.1)
        self.status.configure(text="Status : Validating Email...")

        parsed = parse_email(email)

        if not parsed["success"]:
            self.results.insert(END, parsed["error"])
            self.status.configure(text="Status : Invalid Email")
            self.progress.set(0)
            return

        data = parsed["data"]

        username = data["username"]
        domain = data["domain"]
        tld = data["tld"]

        self.progress.set(0.25)
        self.status.configure(text="Status : Searching GitHub...")

        github = github_lookup(username)

        self.progress.set(0.50)
        self.status.configure(text="Status : Fetching WHOIS...")

        whois = whois_lookup(domain)

        self.progress.set(0.75)
        self.status.configure(text="Status : Fetching DNS Records...")

        dns = get_dns_records(domain)

        self.progress.set(0.90)
        self.status.configure(text="Status : Resolving IP Address...")

        ip = get_ip(domain)

        if ip is None:
          ip = "Not Found"

        self.progress.set(1)

        self.status.configure(text="Status : Analysis Completed")

        self.results.insert(END, "========== EMAIL ==========\n\n")

        self.results.insert(END, f"Email      : {email}\n")
        self.results.insert(END, f"Username   : {username}\n")
        self.results.insert(END, f"Domain     : {domain}\n")
        self.results.insert(END, f"TLD        : {tld}\n")
        self.results.insert(END, f"IP Address : {ip}\n\n")

        self.results.insert(END, "========== GITHUB ==========\n\n")

        if github["success"]:

            info = github["github_info"]

            for key, value in info.items():
                self.results.insert(
                    END,
                    f"{key.replace('_',' ').title()} : {value}\n"
                )

        else:
            self.results.insert(END, github["error"] + "\n")

        self.results.insert(END, "\n")

        self.results.insert(END, "========== WHOIS ==========\n\n")

        if whois["success"]:

            self.results.insert(
                END,
                f"Registrar : {whois['registrar']}\n"
            )

            self.results.insert(
                END,
                f"Creation Date : {whois['creation_date']}\n"
            )

            self.results.insert(
                END,
                f"Expiration Date : {whois['expiration_date']}\n"
            )

            self.results.insert(
                END,
                f"Name Servers : {whois['name_servers']}\n"
            )

        else:

            self.results.insert(
                END,
                whois["error"] + "\n"
            )

        self.results.insert(END, "\n")

        self.results.insert(END, "========== DNS RECORDS ==========\n\n")

        if dns["success"]:

            for record, values in dns["dns_records"].items():

                self.results.insert(
                    END,
                    f"{record} Records\n"
                )

                for value in values:
                    self.results.insert(
                        END,
                        f"   {value}\n"
                    )

                self.results.insert(END, "\n")

        else:

            self.results.insert(
                END,
                dns["error"] + "\n"
            )


    def clear_results(self):

        self.email_entry.delete(0, END)

        self.results.delete("1.0", END)

        self.progress.set(0)

        self.status.configure(text="Status : Waiting...")

    def run(self):
        self.root.mainloop()