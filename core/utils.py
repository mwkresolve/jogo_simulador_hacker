import ipaddress
import random

def generate_unique_ip():
    ip = ipaddress.IPv4Address(random.randint(0, 2**32-1))
    return str(ip)
