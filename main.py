def encrypt(text, shift):
    result = ""
    for char in text:
        if 'a' <= char <= 'z':
            shiftedChar = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        elif 'A' <= char <= 'Z':
            shiftedChar = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            shiftedChar = char
        result += shiftedChar
    return result

originalText = input("Enter the text to encrypt: ")
shiftValue = int(input("Enter the shift value: "))
encryptedText = encrypt(originalText, shiftValue)
print("Encrypted text:", encryptedText)