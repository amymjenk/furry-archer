__author__ = 'amy'

shift = 0
key = {}
decrypt = {}
loweralphabet = 'abcdefghijklmnopqrstuvwxyz'
upperalphabet = loweralphabet.upper()
letters = [loweralphabet, upperalphabet]
alphas = []



def decrypt_key(alphas):

    return decrypt_key

def encrypt_message(crypt, message):
    encrypted = ''
    for l in range(len(message)):
        letter = message[l]
        if letter in crypt:
            encrypted = encrypted + crypt[letter]
        else:
            encrypted = encrypted + letter
    return encrypted

def decrypt_message(crypt, encrypted):

    return message

encrypt_key(letters)
print key
#reverse_key(key)
#print reverse_key
#string = raw_input('What would you like encrypted? ')
#print encrypt(key, string)

print key.items()