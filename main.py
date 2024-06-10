def main():
    while True:
        try:
            operation = input("Choose operation (Encryption/Decryption, or 'exit' to terminate): ").strip().lower()
            if operation == 'exit':
                print("Terminating the program.")
                break
            elif operation not in ['encryption', 'decryption']:
                raise ValueError("Invalid operation. Please enter 'Encryption' or 'Decryption'.")

            text = input("Enter the text: ").strip()
            if not text.isascii():
                raise ValueError("Invalid text. Please enter ASCII characters only.")

            shift = int(input("Enter the shift value (integer): ").strip())

            if operation == 'encryption':
                result = caesar_cipher(text, shift, 'encrypt')
            else:
                result = caesar_cipher(text, shift, 'decrypt')

            print(f"Result: {result}")
        except ValueError as e:
