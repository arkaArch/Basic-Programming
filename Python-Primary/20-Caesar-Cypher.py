from string import ascii_lowercase
letters = list(ascii_lowercase)

def caesar_cypher_encrypt(msg, key):
    encrypted_msg = ''
    # Change the msg to lowercase
    for i in range(len(msg)):
        if msg[i].lower() in letters:
            # Check if the letter is in uppercase
            was_upper = msg[i].isupper()
            # Find the index of letter in letters list
            index = letters.index(msg[i].lower())
            # If the new letter index > len(letters) it starts 
            # form 0 again. That's why modulo len(letters) is required
            new_letter = letters[(index + key) % len(letters)]
            if was_upper: new_letter = new_letter.upper()
            encrypted_msg += new_letter
        # if character is not an alphabet  
        else:
            encrypted_msg += msg[i]
    return encrypted_msg


def caesar_cypher_decrypt(msg, key):
    decrypted_msg = ''
    for i in range(len(msg)):
        if msg[i].lower() in letters:
            was_upper = msg[i].isupper()
            index = letters.index(msg[i].lower())
            new_letter = letters[(index - key) % len(letters)]
            if was_upper: new_letter = new_letter.upper() 
            decrypted_msg += new_letter
        else:
            decrypted_msg += msg[i]
    return decrypted_msg

enc_msg = caesar_cypher_encrypt("How aRe you", 5)
dec_msg = caesar_cypher_decrypt("Mtb fWj dtz", 5)

print(enc_msg)
print(dec_msg)
