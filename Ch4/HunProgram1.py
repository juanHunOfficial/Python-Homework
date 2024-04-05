#Author: Hun, Juan P.

distance_value = int(input("Enter the cipher number you wish to use for you message: "))
message_to_encrypt = input("Enter your message: ")

def caesar_cipher(message_to_encrypt, distance_value):

    encrypted_message = ""

    for char in message_to_encrypt:
        ordvalue = ord(char)
        if ordvalue == ord(" "):
            encrypted_message += chr(ordvalue)
            continue
        cipher_value = ordvalue + distance_value
        if cipher_value > ord("z"):
            cipher_value = ord("a") + distance_value

        encrypted_message += chr(cipher_value)

    return encrypted_message

print(caesar_cipher(message_to_encrypt, distance_value))