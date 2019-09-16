e = x
n = x
c = x
p = x
q=x
phi=(p-1)*(q-1)
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

d = modinv(e,phi)
m =pow(c,d,n)
print(hex(m)[2:-1].decode("hex"))
