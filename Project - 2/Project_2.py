def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = 65 if char.isupper() else 97
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char  # spaces/punctuation as-is
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)  # reverse shift

# Main
text = input("Enter text: ")
shift = int(input("Enter shift key (e.g. 3): "))

encrypted = caesar_encrypt(text, shift)
decrypted = caesar_decrypt(encrypted, shift)

print(f"\nOriginal:  {text}")
print(f"Encrypted: {encrypted}")
print(f"Decrypted: {decrypted}")