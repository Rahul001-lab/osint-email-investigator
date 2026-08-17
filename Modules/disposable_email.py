def disposable_email(email):

    disposable_domains = [
        "10minutemail.com",
        "guerrillamail.com",
        "mailinator.com",
        "tempmail.org"
    ]

    domain = email.split("@")[1].lower()

    return domain in disposable_domains