#Cryptography with Python: Caeser Cipher

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

 # encryption
def encrypt_message(user_message, user_shift_number):
    cipher_message = ''
    for char in user_message:
        
        if char in alphabet:

            position = alphabet.index(char)
            shift_position = position + user_shift_number
            # print(f"{char} - {position} - {shift_position}")
            while shift_position > 25:
                shift_position = shift_position - len(alphabet)
            new_char = alphabet[shift_position]
            cipher_message += new_char
        
        else:
            cipher_message += char
    return f"Encrypted message : {cipher_message}"

 # decryption
def dencrypt_message(user_message, user_shift_number):
    message = ''
    for char in user_message:
        if char in alphabet:
            position = alphabet.index(char)
            shifted_position = position - user_shift_number
            while shifted_position < 0:
                shifted_position = shifted_position + len(alphabet)
            # print(char, position)
            letter = alphabet[shifted_position]
            message += letter
        else:
            message += char

    return f"The Decrypted Message: {message}"




finish_program = False
while not finish_program:

    enc_or_dec = input("Type 'E' to encrypt, type 'D' to decrypt:\n").upper()
    message = input("Enter your message:\n").upper()
    shift_number = int(input("Enter the shift number:\n"))

    if enc_or_dec == 'E':
        encoded_message = encrypt_message(message, shift_number)
        print(encoded_message)
    else:
        decoded_message = dencrypt_message(message, shift_number)
        print(decoded_message)
    restart = input("Type 'Y' to continue, 'N' to exit\n").upper()
    if restart == 'N':
        finish_program = True
        print("\nThank you!")