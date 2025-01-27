import random
import string

#variable characters to categorize the characters
chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

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
    
print(f"original message : {plain_text}")
print(f"encrypted message : {encrypted_text}")


#print the encrypted word and the randomized characters

#write the date encrypted word, and the randomized characters in a .txt file document for safekeep 