import socket

def get_ip(domain):

    try:

        resolved_ip = socket.gethostbyname(domain)
        return resolved_ip

    except socket.gaierror:
        return None