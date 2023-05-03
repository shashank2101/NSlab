import hashlib
import random

# Generate a DSA key pair using SHA-1
def generate_keypair(p, q, g):
    # Generate a random private key x
    x = random.randint(1, q - 1)
    x=3

    # Calculate the public key y
    y = pow(g, x, p)

    return (x, y)

# Sign a message using SHA-1 and DSA
def sign_message(message, p, q, g, x):
    # Compute the SHA-1 hash of the message
    hash_message = hashlib.sha1(message).digest()

    # Generate a random k between 1 and q-1
    k = random.randint(1, q - 1)
    k=3

    # Compute r and s
    r = pow(g, k, p) % q
    s = (x * r + int.from_bytes(hash_message, byteorder='big')) * pow(k, q - 2, q) % q

    return (r, s)

# Verify a DSA signature using SHA-1
def verify_signature(message, signature, p, q, g, y):
    # Compute the SHA-1 hash of the message
    hash_message = hashlib.sha1(message).digest()

    # Extract r and s from the signature
    r, s = signature

    # Verify that 0 < r < q and 0 < s < q
    if r <= 0 or r >= q or s <= 0 or s >= q:
        return False

    # Compute w, u1, and u2
    w = pow(s, q - 2, q)
    u1 = int.from_bytes(hash_message, byteorder='big') * w % q
    u2 = r * w % q

    # Compute v
    v = pow(g, u1, p) * pow(y, u2, p) % p % q

    # The signature is valid if v = r
    return v == r

# Example usage
p = 101
q = 7   
g = 2
(x, y) = generate_keypair(p, q, g)
print(x)
message = b"Hello, world!"
signature = sign_message(message, p, q, g, x)
print("Signature:", signature)

# Verify the signature
is_valid = verify_signature(message, signature, p, q, g, y)
print("Is the signature valid?", is_valid)
