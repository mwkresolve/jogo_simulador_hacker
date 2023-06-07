import ipaddress
import random
import string

def generate_unique_ip():
    ip = ipaddress.IPv4Address(random.randint(0, 2**32-1))
    return str(ip)

def generate_random_password():
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(8))
    return password
