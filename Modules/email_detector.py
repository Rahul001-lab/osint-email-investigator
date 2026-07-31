from modules.parser import parse_email
from modules.github_intel import github_lookup
from modules.whois_lookup import whois_lookup
from modules.dns_info import get_dns_records
from modules.dns_lookup import get_ip


def investigate_email(email):

    parsed = parse_email(email)

    if not parsed["success"]:
        return parsed

    data = parsed["data"]

    username = data["username"]
    domain = data["domain"]
    tld = data["tld"]

    github = github_lookup(username)
    whois = whois_lookup(domain)
    dns = get_dns_records(domain)
    ip = get_ip(domain)

    return {
        "success": True,
        "email_info": data,
        "github": github,
        "whois": whois,
        "dns": dns,
        "ip": ip
    }