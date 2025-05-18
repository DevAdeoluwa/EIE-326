def encrypt(text, shift):
    """Encrypt the text using the Caesar cipher."""
    result = ""
    for char in text:
        if char.isalpha():  # Check if character is a letter
            shift_base = 65 if char.isupper() else 97
            # Encrypt character and wrap around the alphabet
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char  # Non-alphabetical characters remain unchanged
    return result

def decrypt(text, shift):
    """Decrypt the text using the Caesar cipher."""
    return encrypt(text, -shift)

def main():
    text = input("Enter the text: ")
    shift = int(input("Enter the shift (positive for encryption, negative for decryption): "))
    
    if shift > 0:
        result = encrypt(text, shift)
        print(f"Encrypted text: {result}")
    else:
        result = decrypt(text, abs(shift))
        print(f"Decrypted text: {result}")

if __name__ == "__main__":
    main()