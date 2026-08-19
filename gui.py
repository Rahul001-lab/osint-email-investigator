import customtkinter as ctk
from tkinter import END
import threading

from modules.email_detector import investigate_email


class EmailOSINTGUI:

    def __init__(self):

        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("blue")

        self.root = ctk.CTk()

        self.root.title("Email OSINT Investigator")
        self.root.geometry("900x650")
        self.root.resizable(False, False)

        self.create_widgets()

    def create_widgets(self):

        self.title = ctk.CTkLabel(
            self.root,
            text="EMAIL OSINT INVESTIGATOR",
            font=("Arial", 28, "bold")
        )

        self.title.pack(pady=20)

        self.input_frame = ctk.CTkFrame(self.root)

        self.input_frame.pack(fill="x", padx=20)

        self.email_entry = ctk.CTkEntry(
            self.input_frame,
            width=500,
            placeholder_text="Enter Email Address"
        )

        self.email_entry.pack(side="left", padx=10, pady=10)

        self.analyze_button = ctk.CTkButton(
            self.input_frame,
            text="Analyze",
            command=self.analyze_email
        )

        self.analyze_button.pack(side="left", padx=5)

        self.clear_button = ctk.CTkButton(
            self.input_frame,
            text="Clear",
            command=self.clear_results
        )

        self.clear_button.pack(side="left", padx=5)

        self.results = ctk.CTkTextbox(
            self.root,
            width=850,
            height=430
        )

        self.results.pack(padx=20, pady=20)

        self.status = ctk.CTkLabel(
            self.root,
            text="Status : Ready"
        )

        self.status.pack(pady=10)

    def analyze_email(self):

        self.results.delete("1.0", END)

        email = self.email_entry.get().strip()

        if not email:
            self.status.configure(
                text="Status : Please enter an email address."
            )
            return

        self.status.configure(
            text="Status : Investigating..."
        )

        self.analyze_button.configure(
            state="disabled"
        )

        threading.Thread(
            target=self.run_investigation,
            args=(email,),
            daemon=True
        ).start()

    def run_investigation(self, email):

        try:

            result = investigate_email(email)

            self.root.after(
                0,
                lambda: self.display_results(result)
            )

        except Exception as e:

            error_message = str(e)

            self.root.after(
                          0,
                     lambda: self.show_error(error_message)
                     )

    def display_results(self, result):

        if not result["success"]:

            self.results.insert(
                END,
                result["error"]
            )

            self.status.configure(
                text="Status : Failed"
            )

            self.analyze_button.configure(
                state="normal"
            )

            return

        # Email Information Module

        email_info = result["email_info"]

        self.results.insert(
            END,
            "========== EMAIL ==========\n\n"
        )

        self.results.insert(
            END,
            f"Email      : {email_info['email']}\n"
        )

        self.results.insert(
            END,
            f"Username   : {email_info['username']}\n"
        )

        self.results.insert(
            END,
            f"Domain     : {email_info['domain']}\n"
        )

        self.results.insert(
            END,
            f"TLD        : {email_info['tld']}\n\n"
        )

        # GitHub Intelligence Module

        self.results.insert(
            END,
            "========== GITHUB ==========\n\n"
        )

        github = result["github"]

        if github["success"]:

            for key, value in github["github_info"].items():

                self.results.insert(
                    END,
                    f"{key.replace('_', ' ').title()} : {value}\n"
                )

        else:

            self.results.insert(
                END,
                github["error"] + "\n"
            )

        self.results.insert(
            END,
            "\n========== WHOIS ==========\n\n"
        )

        # WHOIS Module

        whois = result["whois"]

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

        self.results.insert(
            END,
            "\n========== DNS ==========\n\n"
        )

        # DNS Module

        dns = result["dns"]

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

                self.results.insert(
                    END,
                    "\n"
                )

        else:

            self.results.insert(
                END,
                dns["error"] + "\n"
            )

        self.results.insert(
            END,
            "\n========== IP ==========\n\n"
        )

        self.results.insert(
            END,
            f"{result['ip']}\n"
        )

        # Geolocation Module

        self.results.insert(
            END,
            "\n========== GEOLOCATION ==========\n\n"
        )

        geolocation = result["geolocation"]

        if geolocation["success"]:

            self.results.insert(
                END,
                f"Country : {geolocation['country']}\n"
            )

            self.results.insert(
                END,
                f"Region : {geolocation['region']}\n"
            )

            self.results.insert(
                END,
                f"City : {geolocation['city']}\n"
            )

            self.results.insert(
                END,
                f"ZIP : {geolocation['zip']}\n"
            )

            self.results.insert(
                END,
                f"Latitude : {geolocation['lat']}\n"
            )

            self.results.insert(
                END,
                f"Longitude : {geolocation['lon']}\n"
            )

            self.results.insert(
                END,
                f"Timezone : {geolocation['timezone']}\n"
            )

            self.results.insert(
                END,
                f"ISP : {geolocation['isp']}\n"
            )

        else:

            self.results.insert(
                END,
                geolocation["error"] + "\n"
            )

        # GitLab Module

        self.results.insert(
            END,
            "\n========== GITLAB ==========\n\n"
        )

        gitlab = result["gitlab"]

        if gitlab["success"]:

            info = gitlab["gitlab_info"]

            for key, value in info.items():

                self.results.insert(
                    END,
                    f"{key.replace('_', ' ').title()} : {value}\n"
                )

        else:

            self.results.insert(
                END,
                gitlab["error"] + "\n"
            )

        # Sherlock Module

        self.results.insert(
            END,
            "\n========== SHERLOCK ==========\n\n"
        )

        sherlock = result["sherlock"]

        if sherlock["success"]:

            self.results.insert(
                END,
                sherlock["sherlock_output"] + "\n"
            )

        else:

            self.results.insert(
                END,
                sherlock["error"] + "\n"
            )

        self.status.configure(
            text="Status : Completed"
        )

        self.analyze_button.configure(
            state="normal"
        )

    def show_error(self, error):

        self.results.delete("1.0", END)

        self.results.insert(
            END,
            f"Error : {error}"
        )

        self.status.configure(
            text="Status : Failed"
        )

        self.analyze_button.configure(
            state="normal"
        )

    def clear_results(self):

        self.email_entry.delete(0, END)

        self.results.delete("1.0", END)

        self.status.configure(
            text="Status : Ready"
        )

        self.analyze_button.configure(
            state="normal"
        )

    def run(self):

        self.root.mainloop()