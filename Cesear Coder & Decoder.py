def caesar_cipher(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            result += char

    return result

# Get user input for encoding or decoding
choice = input("Enter 'E' to encode or 'D' to decode: ")

if choice.lower() == 'e':
    # Encoding mode
    text = input("Enter the text to encode: ")
    shift = int(input("Enter the shift number: "))

    encoded_text = caesar_cipher(text, shift)
    print("Encoded text:", encoded_text)

elif choice.lower() == 'd':
    # Decoding mode
    text = input("Enter the text to decode: ")
    shift = int(input("Enter the shift number: "))

    decoded_text = caesar_cipher(text, -shift)
    print("Decoded text:", decoded_text)

else:
    print("Invalid choice. Please enter 'E' or 'D'.")
