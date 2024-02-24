from load_image import ft_load
from pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("arg img is necessary")
        exit()
    array = ft_load(sys.argv[1])
    if array is None:
        exit()
    ft_invert(array)
    ft_red(array)
    ft_green(array)
    ft_blue(array)
    ft_grey(array)
    print(ft_invert.__doc__)
