
substitutionEncryptMap = {
    "A" : "V",
    "B" : "8",
    "C" : "2",
    "D" : "P",
    "E" : "3",
    "F" : "E",
    "G" : "9",
    "H" : "+", # added as a single "+"" instead of "++"
    "I" : "!",
    "K" : "<",
    "J" : "&",
    "L" : "7",
    "M" : "W",
    "N" : "Z",
    "O" : "@",
    "P" : "₱",
    "Q" : "6",
    "R" : "F",
    "S" : "5",
    "T" : "L",
    "U" : "(",
    "V" : "^", # added value was not on the original instruction map
    "W" : "M",
    "X" : "*",
    "Y" : "?",
    "Z" : "0",
    "0" : "C",
    "1" : "I",
    "2" : "S",
    "3" : "B",
    "4" : "Y",
    "5" : "G",
    "7" : "T",
    "8" : "$",
    "9" : "Q"
}
substitutionDecryptMap = {value:key for key,value in substitutionEncryptMap.items()}



# main functions #

def expandedEncrypt(plaintext : str):
    result = ""
    for i in plaintext:
        result += substitutionEncryptMap[i]
    return result
def expandedDecrypt(plaintext : str):
    result = ""
    for i in plaintext:
        result += substitutionDecryptMap[i]
    return result

# main functions #


# concise version #
def loopedEncrypt(plaintext : str ):
    return "".join([substitutionEncryptMap[i] for i in plaintext])
def loopedDecrypt(plaintext : str):
    return "".join([substitutionDecryptMap[i] for i in plaintext])
def translatedEncrypt(plaintext:str):
	return plaintext.translate(str.maketrans(substitutionEncryptMap))
def translatedDecrypt(plaintext:str):
	return plaintext.translate(str.maketrans(substitutionDecryptMap))
# concise version #



def testCase(plaintext_test_case,encrypt, decrypt, test_case_name = None):
    if test_case_name != None:
        print(test_case_name)
    print("Plaintext:",  plaintext_test_case)
    encryptedText = encrypt(plaintext_test_case)
    print("Encrypted", encryptedText)
    print()
    print("Encrypted Text:", encryptedText)
    print("Decrypted:", decrypt(encryptedText))
    print()



# Test Cases #
def loopedEncryptAndDecryptTestCase(plaintext):
    return testCase(plaintext, loopedEncrypt, loopedDecrypt)
def translatedEncryptAndDecryptTestCase(plaintext):
    return testCase(plaintext, translatedEncrypt, translatedDecrypt)
def expandedEncryptAndDecryptTestCase(plaintext):
    return testCase(plaintext, expandedEncrypt, expandedDecrypt)
# Test Cases #
import re
def modifiedInput():
    inp = input("Password:")
    while re.match("^(?=.*\d)(?=.*[A-Z])[A-Z0-9]{7,15}$", inp) == None:
        print("must be at least 7 characters, contains an uppercase and a digit, and must not exceed 15 characters")
        inp = input("Password:")
    return inp
def main():
    # test_case = "LOVEYOU2"
    user_input = modifiedInput()
    # loopedEncryptAndDecryptTestCase(test_case)
    # translatedEncryptAndDecryptTestCase(test_case)

    # go to comment with `main functions` for the used functions in this test case
    expandedEncryptAndDecryptTestCase(user_input)


if __name__ == "__main__":
    main()
