import string
import random
normalText = string.ascii_uppercase + string.digits
def makeCaesarMap(shift):
    shift %= len(normalText)
    caesarMap = normalText[shift:] + normalText[:shift]
    return caesarMap
def makeTranslation(keys, values):
    return str.maketrans(dict(zip(keys,values)))
def encrypt(plaintext : str,shift = random.randrange(36)):
    caesarMap = makeCaesarMap(shift)
    encrypted = plaintext.translate(makeTranslation(normalText, caesarMap))
    return (encrypted,shift)
def decrypt(encryptedText, shift):
    caesarMap = makeCaesarMap(shift)
    decrypted = encryptedText.translate(makeTranslation(caesarMap, normalText))
    return decrypted

class CeasarMap:
    def __init__(self, shift):
        caesarMap = makeCaesarMap(shift)
        self.encryptMap = makeTranslation(normalText, caesarMap)
        self.decryptMap = makeTranslation(caesarMap, normalText)
    def encrypt(self, plaintext : str):
        return plaintext.translate(self.encryptMap)
    def decrypt(self, encryptedText : str):
        return encryptedText.translate(self.decryptMap)

import re
def modifiedInput():
    inp = input("Password: ")
    while re.match("^(?=.*\d)(?=.*[A-Z])[A-Z0-9]{7,15}$", inp) == None:
        inp = input("Password: ")
    return inp


def main():
    caesarCipher = CeasarMap(4)

    user_input = modifiedInput()

    encryptedText = caesarCipher.encrypt(user_input)
    decryptedText = caesarCipher.decrypt(encryptedText)
    print(encryptedText, decryptedText)
    return


main()