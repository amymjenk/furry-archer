__author__ = 'amy'

# this code will be the functions to generate encode and decode keys as a polyalphabetic cipher, a repeating
# cipher of the same string

def encrypt(alphas):    # create encryption/decryption key generation
    cipher = raw_input('What is the codeword? ')    # the password the data will be encrypted with
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