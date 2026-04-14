from sympy import *
import random


def randcoprime(n, limlow=(10**3), limHigh=(10**10)):
    while True:
        candidate = random.randint(limlow, limHigh)
        if gcd(candidate, n) == 1:
            return candidate


def modinv(e, phi):
    d_old = 0; r_old = phi
    d_new = 1; r_new = e
    while r_new > 0:
        a = r_old // r_new
        (d_old, d_new) = (d_new, d_old - a * d_new)
        (r_old, r_new) = (r_new, r_old - a * r_new)
    return d_old % phi if r_old == 1 else None


def keyGen():
    prime1 = randprime(10**5, 10**10)
    prime2 = randprime(10**5, 10**10)
    print(prime1)
    print(prime2)
    publicMod = prime1*prime2
    print(publicMod)
    privateMod = (prime1 - 1) * (prime2 - 1)
    print(privateMod)
    publicKey = randcoprime(privateMod)
    print(publicKey)
    privateKey = modinv(publicKey,privateMod)
    print(privateKey)


if __name__ == "__main__":
    keyGen()


# (n * pri
