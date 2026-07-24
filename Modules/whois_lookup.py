import whois

def whois_lookup(domain):

    try:
        whois_data = whois.whois(domain)

        registrar = whois_data.get("registrar")
        creation_date = whois_data.get("creation_date")
        expiration_date = whois_data.get("expiration_date")
        name_servers = whois_data.get("name_servers")

        return {
            "success": True,
            "registrar": registrar,
            "creation_date": creation_date,
            "expiration_date": expiration_date,
            "name_servers": name_servers
        }

    except Exception as e:
        return {
            "success": False,
            "error": "Unable to fetch WHOIS information."
        }