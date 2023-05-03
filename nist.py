import hashlib
import random

def gcd(a, b):
    """Compute the Greatest Common Divisor of two integers."""
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    """Compute the modular inverse of an integer a modulo m."""
    if gcd(a, m) != 1:
        raise ValueError("The modular inverse does not exist.")
    b, c = m, a
    x0, x1 = 0, 1
    while c != 0:
        q, r = divmod(b, c)
        x0, x1 = x1 - q*x0, x0
        b, c = c, r
    return x1 % m

def generate_keypair(p, q, g):
    """Generate a new DSA key pair."""
    x = random.randint(1, q-1)
    y = pow(g, x, p)
    return (x, y)

def sign_message(message, p, q, g, x):
    """Sign a message using the DSA algorithm."""
    h = int.from_bytes(hashlib.sha256(message).digest(), byteorder="big")
    # print(h)
    k = random.randint(1, q-1)
    r = pow(g, k, p) % q
    s = (mod_inverse(k, q) * (h + x*r)) % q
    # print(r,s)
    return (r, s)

def verify_signature(message, signature, p, q, g, y):
    """Verify the signature of a message using the DSA algorithm."""
    h = int.from_bytes(hashlib.sha256(message).digest(), byteorder="big")
    # print(h)
    r, s = signature
    w = mod_inverse(s, q)
    u1 = (h * w) % q
    u2 = (r * w) % q
    v1=pow(g,u1,p)
    v2=pow(y,u2,p)
    v=v1*v2
    v=v%q

    return v1==r
# Example usage:
p = 189028452528179231401094601980440044647329953293619004566990361661939881707620657153460287188910681147482026868523622080905883085834651272891318080718879726942463175248050208821703078763559809487932981975284873786862949304269933116267826400033356468081735088475481358354123245874989000626069609329695649838847981107
q = 970964596122503009724441967171755384916373390209
g = 2147483647
(x, y) = generate_keypair(p, q, g)
message = b"This is a test message."
signature = sign_message(message, p, q, g, x)
print(verify_signature(message, signature, p, q, g, y))
