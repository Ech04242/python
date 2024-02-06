import sys

if __name__ == "__main__":
    if (len(sys.argv) > 2):
        print("AssertionError")
        exit

    if (len(sys.argv) == 2):
        string = sys.argv[1]
    else:
        print("What is the text to count?")
        string = input()
    low = 0
    upp = 0
    car = 0
    pun = 0
    spa = 0
    dig = 0
    for value in string:
        if (value.isupper()):
            upp += 1
        elif (value.islower()):
            low += 1
        elif (value.isdigit()):
            dig += 1
        elif (value.isspace()):
            spa += 1
        else:
            pun += 1
        car += 1
    print(f"The text contains {car} characters:")
    print(f"{upp} upper letters")
    print(f"{low} lower letters")
    print(f"{pun} punctuation marks")
    print(f"{spa} spaces")
    print(f"{dig} digits")
