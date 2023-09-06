import re
import sys
def input2(text : str = "", re_pattern : str = None, err_msg : str = ""):
    if type(re_pattern) != str:
        return input(text)
    temp = input(text)
    while re.match(re_pattern, temp) == None:
        sys.stderr.write(err_msg)
        temp = input(text)
    return temp

# sort while the input is still string
# and parse it as int
def sortInt(arr,/, isReversed):
    return int("".join(sorted(arr,reverse=isReversed)))

def largestPossibleInt(arr : list):
    return sortInt(arr, isReversed=True)
def smallestPossibleInt(arr :list):
    return sortInt(arr, isReversed=False)

# if let's say an array/list of integer was passed we could do it this way
# sort it by number 1 ... 9 or 9 ... 1
# and convert it into a 10 based number
def sortInt2(arr,/,isReversed):
    temp = 0
    arr = sorted(arr, reverse=isReversed)
    for i in range(len(arr)):
        temp += arr[i] * 10 ** i
    return temp
def largestPossibleInt2(arr : list):
    return sortInt2(arr, isReversed=False)
def smallestPossibleInt2(arr :list):
    return sortInt2(arr, isReversed=True)


def main():
    arr = [input2(f"Number {i}: ","^\d$","Invalid Input, must only have a single digit character\n") for i in range(1, 6)]
    print()
    print("output if inputs are a string, (uses sortInt())")
    print(f"largest: {largestPossibleInt(arr):,}", f"smallest: {smallestPossibleInt(arr):,}")
    print()

    arr_int = list(map(int, arr))
    print("output if inputs are an integer, (uses sortInt2())")
    print(f"largest: {largestPossibleInt2(arr_int):,}", f"smallest: {smallestPossibleInt2(arr_int):,}")


if __name__ == "__main__":
    main()