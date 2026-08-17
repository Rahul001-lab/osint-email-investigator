from modules.parser import parse_email
from modules.github_intel import github_lookup
from modules.whois_lookup import whois_lookup
from modules.dns_info import get_dns_records
from modules.dns_lookup import get_ip
from modules.geolocation import get_geolocation
from modules.gitlab_lookup import gitlab_lookup
from modules.sherlock_lookup import sherlock_lookup
from modules.disposable_email import disposable_email

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
    geolocation = get_geolocation(ip)
    gitlab = gitlab_lookup(username)
    sherlock = sherlock_lookup(email)
    disposable_email = disposable_email(email
                                        )
    return {
        "success": True,
        "email_info": data,
        "github": github,
        "whois": whois,
        "dns": dns,
        "ip": ip,
        "geolocation": geolocation,
        "gitlab": gitlab,
        "sherlock": sherlock,
        "disposable": disposable_email
    }