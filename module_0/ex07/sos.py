import sys

if __name__ == "__main__":
    dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
        'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
        'Z': '--..', ' ': '/',
        '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
        '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'
    }

    if (len(sys.argv) != 2):
        print("error : too many arguments")
        exit(0)
    try:
        res = ""
        for i in sys.argv[1]:
            if i not in dict:
                raise KeyError("an value is not on morse dict")
            res = res + dict[i] + " "
        res = res[:-1]
        print(res)
    except ValueError:
        print("AssertionError: bad value")
    except KeyError as error:
        print("AssertionError:", error)
