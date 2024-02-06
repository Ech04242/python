import sys
from ft_filter import ft_filter


if __name__ == "__main__":
    try:
        if len(sys.argv) != 3:
            raise AssertionError("the arguments are bad")

        text = sys.argv[1]
        nb = int(sys.argv[2])

        if not isinstance(nb, int) or not isinstance(text, str):
            raise AssertionError("Invalid argument type")
        result = list(ft_filter(lambda word: len(word) > nb, text.split()))
        print(result)
    except ValueError:
        print("AssertionError: bad int value ( you re an idiot )")
    except AssertionError as error:
        print("AssertionError:", error)
