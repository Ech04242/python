import sys

if __name__ == "__main__":
    argc = len(sys.argv)
    if (argc <= 1):
        print()
        sys.exit(0)
    elif (argc >= 3):
        print("AssertionError: more than one argument is provided")
    elif (argc == 2):
        try:
            nb = int(sys.argv[1])
            if (nb % 2 == 0):
                print("I'm Even")
            else:
                print("I'm Odd")
        except (ValueError):
            print("AssertionError: argument is not an integer")
