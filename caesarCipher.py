import string
normalText = string.ascii_uppercase + string.digits
def makeCaesarMap(rotation):
    rotation %= len(normalText)
    caesarMap = normalText[rotation:] + normalText[:rotation]
    return (caesarMap,rotation)

def main():
    return


main()