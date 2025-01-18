# Ceaser Cypher Algorithm
# Well defined key of value 3. 
# Add 3 at encoder to get cipher text from plain text and subtract 3 at decoder to get plain text back from cipher text.

def encrypt(plain_text,key):
    cipher = ""

    for i in range(len(plain_text)):
        ch = plain_text[i]
    
        if(ch.isupper()):
            cipher += chr((ord(ch) + key - 65) % 26 + 65) 
            # Add key value and subtract 65 (corresponding to ASCII of "A") to get character in range of  0 to 25. 
            # Modulo 26 applies the shift within a circular range of 26 letters (A-Z).
            # Add Back 26 to get back ASCII value of encrypted character
        else:
            cipher += chr((ord(ch) + key - 97) % 26 + 97)
            # Add key value and subtract 97 (correspoding to ASCII of "a") to get character in range of  0 to 25.
    return cipher
        
plain_text = input("Enter text you want to encrypt \n")
key = 3
print("Cipher Text = " + encrypt(plain_text,key))