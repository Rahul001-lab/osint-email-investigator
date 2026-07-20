import customtkinter as ctk


class EmailOSINTGUI:
    def __init__(self):
        # Theme
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Main Window
        self.root = ctk.CTk()
        self.root.title("OSINT Email Investigator")
        self.root.geometry("900x650")
        self.root.resizable(False, False)

        self.create_widgets()

    def create_widgets(self):

        # ==========================
        # Title
        # ==========================
        self.title = ctk.CTkLabel(
            self.root,
            text="OSINT EMAIL INVESTIGATOR",
            font=("Arial", 28, "bold")
        )

        self.title.pack(pady=20)

        # ==========================
        # Input Frame
        # ==========================
        self.input_frame = ctk.CTkFrame(self.root)

        self.input_frame.pack(fill="x", padx=20)

        self.email_entry = ctk.CTkEntry(
            self.input_frame,
            width=500,
            placeholder_text="Enter Email Address"
        )

        self.email_entry.pack(side="left", padx=10, pady=10)

        self.analyze_btn = ctk.CTkButton(
            self.input_frame,
            text="Analyze"
        )

        self.analyze_btn.pack(side="left", padx=5)

        self.clear_btn = ctk.CTkButton(
            self.input_frame,
            text="Clear"
        )

        self.clear_btn.pack(side="left", padx=5)

        # ==========================
        # Results Box
        # ==========================
        self.results = ctk.CTkTextbox(
            self.root,
            width=850,
            height=400
        )

        self.results.pack(padx=20, pady=20)

        # ==========================
        # Progress Bar
        # ==========================
        self.progress = ctk.CTkProgressBar(self.root)

        self.progress.pack(fill="x", padx=20)

        self.progress.set(0)

        # ==========================
        # Status
        # ==========================
        self.status = ctk.CTkLabel(
            self.root,
            text="Status : Ready"
        )

        self.status.pack(pady=10)

    def run(self):
        self.root.mainloop()