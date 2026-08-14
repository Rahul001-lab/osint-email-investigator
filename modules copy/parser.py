import re


def validate_email(email):
    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
    return re.match(pattern, email) is not None


def extract_username(email):
    return email.split("@")[0]


def extract_domain(email):
    return email.split("@")[1]


def extract_tld(domain):
    return domain.split(".")[-1]


def parse_email(email):

    if not validate_email(email):
        return {
            "success": False,
            "error": "Invalid email format"
        }

    username = extract_username(email)
    domain = extract_domain(email)
    tld = extract_tld(domain)

    return {
        "success": True,
        "data": {
            "email": email,
            "username": username,
            "domain": domain,
            "tld": tld
        }
    }


if __name__ == "__main__":
    email = input("Enter Email: ")

    result = parse_email(email)

    if result["success"]:
        print("\n===== Parsed Email =====")

        for key, value in result["data"].items():
            print(f"{key.capitalize()}: {value}")

    else:
        print(result["error"])