import dns.resolver

def get_dns_records(domain):
    try:
        record_types = ["A", "AAAA", "MX", "NS", "TXT"]

        dns_records = {}

        for record_type in record_types:
            ip_addresses = []
            try:

                dns_data = dns.resolver.resolve(domain, record_type)

                for record in dns_data:
                      ip_addresses.append(str(record))

                dns_records[record_type] = ip_addresses

            except Exception:
                continue
        return {
            "success" : True,
            "dns_records": dns_records
        }

    except Exception as e:
        return { 
            "success": False,
            "error": "Unable to fetch DNS records."
        }