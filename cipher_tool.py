import random
import string

# Adding space, punctuation, digits, and alphabets
char = ' ' + string.punctuation + string.digits + string.ascii_letters
char = list(char)  # Create a list of characters

# Create a randomly shuffled key from 'char list'
key = char.copy()
random.shuffle(key)


#Encrypt function 
def encrypt_function():
    text = input('Enter a message to encrypt: ')
    encrypt_text = ""
    for letter in text:
        index_ = char.index(letter)  # Get the index of the letter in char
        encrypt_text += key[index_]  # Use the same index to get the encrypted letter
    print(f'Encrypted message: {encrypt_text}')
    return encrypt_text

#Decrypt function
def decrypt_function(encrypt_text):
    decrypt_text = ""
    for letter in encrypt_text:
        index_ = key.index(letter)  
        decrypt_text += char[index_]  
    print(f'Decrypted message: {decrypt_text}')
    return decrypt_text



def main():
    encrypted_message = ""  # Variable(placholder) to store the encrypted message => 
    

    while True:
        print('-------- Encrypt Message Platform ---------')
        print('1- Encrypt message')
        print('2- Decrypt message')
        print('3- Exit')

        menu = input('Please select: ')

        if menu == '1':
            encrypted_message = encrypt_function()
        elif menu == '2':
            if encrypted_message:
                decrypt_function(encrypted_message)
            else:
                print('No encrypted message found. Please encrypt a message first.')
        elif menu == '3':
            print('Exiting the program.')
            break
        else:
            print('Invalid selection. Please choose a valid option.')

if __name__ == '__main__':
    main()
