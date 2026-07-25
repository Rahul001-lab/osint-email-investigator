import dns.resolver

def get_dns_records(domain):
    try:
        dns_record_A = dns.resolver.resolve(domain, "A")

        ip_addresses = []

        for record in dns_record_A:
            ip_addresses.append(str(record))

        return {
            "success": True,
            "A": ip_addresses
        }

    except Exception as e:
        return { 
            "success": False,
            "error": "Unable to fetch DNS A records."
        }