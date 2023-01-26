import random
import string

def generate_password(length: int) -> str:
    """Generate a random password with specified length"""
    password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(length))
    return password

# Example usage
print(generate_password(12))
