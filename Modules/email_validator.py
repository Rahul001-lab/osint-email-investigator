import validators


def validate_email(email):
    """
    Check whether the email address is valid.
    """
    return validators.email(email)


def extract_username(email):
    """
    Extract the username from an email address.
    """
    return email.split("@")[0]

def extract_domain(email):
    """
    Extract the domain from an email address.
    """
    return email.split("@")[1]

def extract_tld(email):
    """
    Extract the top-level domain (TLD) from an email address.
    """
    return email.split(".")[-1]