__author__ = 'amy'

# this code contains the decrypt and encrypt functions for a 'caesar cipher' which uses an offset of the alphabet.
# other characters remain the same.

def encrypt_key(alphas):    # create encryption/decryption key generation
    shift = int(raw_input('What is the shift? '))
    alpha = ''
    for j in range(len(alphas)):
        alpha = alphas[j]
        for i in range(len(alpha)):
            define = i + shift
            if define >= len(alpha):
                define = define % len(alpha)
            set_letter = str(alpha[define])
            letter = str(alpha[i])
            key[letter] = set_letter

def reverse_key(encode):    # reverses an existing key
    if encode != {}:

        decrypt = {}
        letter = ''
        set_letter = ''

        for i in range(len(encode)):
            letter = encode[i]
            set_letter = get(encode[i])
            decrypt[letter] = set_letter
        print decrypt
    else:
        return 'A key does not exist'