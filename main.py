def encrypt(text):
    TextBinary = int(''.join(format(ord(i), '08b') for i in text))
    print(TextBinary)
    TextBinary = TextBinary * (10 ** 7)
    TextBinary = TextBinary + (10 ** (len(str(TextBinary))))
    TextBinary = str(TextBinary + 1111111)
    print(TextBinary)
    text = ''.join(chr(int(TextBinary[i*8:i*8+8], 2))
                   for i in range(len(TextBinary)//8))
    print(text)
    return (text)


def decrypt(text):
    TextBinary = int(''.join(format(ord(i), '08b') for i in text))
    print(TextBinary)
    TextBinary = TextBinary - 1111111
    print(TextBinary)
    TextBinary = TextBinary - (10 ** (len(str(TextBinary)) - 1))
    print(TextBinary)
    TextBinary = str(TextBinary // (10 ** 7))
    print(TextBinary)
    text = ''.join(chr(int(TextBinary[i*8:i*8+8], 2))
                   for i in range(len(TextBinary)//8))
    print(text)


decrypt(encrypt(input()))
