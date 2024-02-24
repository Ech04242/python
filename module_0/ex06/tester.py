from ft_filter import ft_filter


# returns True if the argument passed is even
def check_even(number):
    if number % 2 == 0:
        return True
    return False


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    if list(ft_filter(check_even, numbers)) \
            == list(filter(check_even, numbers)):
        print("OK !")
    else:
        print("KO !")
