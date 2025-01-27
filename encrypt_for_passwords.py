import random
import string
from datetime import datetime

#date and time
current_datetime = datetime.now()
print("Current date and time:", current_datetime)

#variable characters to categorize the characters
chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

def encryption():

    #encryption
    while True:
        plain_text = input("Kindly put what you want to encrypt: ")
        encrypted_text = ""

        #ask for confirmation
        ask = input("\nAre you sure that is your text for encryption? (y/n)\n")
        if ask != "y":
            continue
        elif ask == "y":
            break

    for letter in plain_text:
        index = chars.index(letter)
        encrypted_text += key[index]

    #print the encrypted word and the randomized characters

    print(f"original message : {plain_text}")
    print(f"encrypted message : {encrypted_text}")

    #write the date encrypted word, and the randomized characters in a .txt file document for safekeep 

    name_for_encrypted = input("Please give a name for your encrypted text:\n")

    with open(".\encryption_storage.txt", "a") as file_handle:
        file_handle.write(f"{name_for_encrypted}, {current_datetime}\n\nencryption alphabet: {key}\n\noriginal message: {plain_text}\nencrypted message: {encrypted_text}\n")

    print("done!")

def decryption():
    #get the encrypted text
    encrypted_text = input("What is your encrypted text?: ")
    #get the randomized encryption alphabet
    #decryption and print it
    print("done!")
