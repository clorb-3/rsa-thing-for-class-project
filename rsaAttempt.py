from sympy import *
import random


def randcoprime(n, limlow=(10**1), limHigh=(10**2)):
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
    prime1 = randprime(10**1, 10**2)
    prime2 = randprime(10**1, 10**2)
    print(prime1)
    print(prime2)
    publicMod = prime1*prime2
    print("n = " + str(publicMod))
    privateMod = (prime1 - 1) * (prime2 - 1)
    publicKey = randcoprime(privateMod)
    print("e = " + str(publicKey))
    privateKey = modinv(publicKey,privateMod)
    print("d = " + str(privateKey))


def encodeDecode(modulus, key, text):
    result = ""
    for i in text:
        char =  pow(ord(i), key, modulus) 
        result += str(char)
    print(result)

    pass


def main():
    if input("genarate keys? \n:> ").strip().lower()[0] == 'y':
        keyGen()
    else:
        encodeDecode(int(input("mod? \n:> ")), int(input("key \n:> ")), input("text? \n:> "))


if __name__ == "__main__":
    main()


# (n * pri
