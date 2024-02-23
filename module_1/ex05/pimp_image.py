import matplotlib.pyplot as plt
import numpy as np


def ft_invert(img: list):
    """ switch all pixel color to negative

    Args:
        img (list): img to invert

    Returns:
        _type_: new img with invert caracteristic
    """
    new_img = np.array(img)
    width, heidth, _ = new_img.shape
    for x in range(heidth):
        for y in range(width):
            new_img[y][x] = 255 - new_img[y][x]
    plt.imshow(new_img)
    plt.show()
    return (new_img)


def ft_red(img: list):
    """ keep only red calque on img

    Args:
        img (list): img to apply calque

    Returns:
        _type_: new img with calque
    """
    width, heidth, _ = img.shape
    new_img = np.array(img)
    for x in range(heidth):
        for y in range(width):
            for z in range(3):
                if z == 0:
                    new_img[y][x][z] = new_img[y][x][z]
                else:
                    new_img[y][x][z] = 0
    plt.imshow(new_img)
    plt.show()
    return (new_img)


def ft_green(img: list):
    """ keep only green calque on img

    Args:
        img (list): img to apply calque

    Returns:
        _type_: new img with calque
    """
    new_img = np.array(img)
    width, heidth, _ = new_img.shape
    for x in range(heidth):
        for y in range(width):
            for z in range(3):
                if z == 1:
                    new_img[y][x][z] = new_img[y][x][z]
                else:
                    new_img[y][x][z] = 0
    plt.imshow(new_img)
    plt.show()
    return (new_img)


def ft_blue(img: list):
    """ keep only blue calque on img

    Args:
        img (list): img to apply calque

    Returns:
        _type_: new img with calque
    """
    new_img = np.array(img)
    width, heidth, _ = new_img.shape
    for x in range(heidth):
        for y in range(width):
            for z in range(3):
                if z == 2:
                    new_img[y][x][z] = new_img[y][x][z]
                else:
                    new_img[y][x][z] = 0
    plt.imshow(new_img)
    plt.show()
    return (new_img)


def ft_grey(img: list):
    """ switch color of image to grey

    Args:
        img (list): img to apply calque

    Returns:
        _type_: new img with calque
    """
    new_img = np.array(img)
    width, heidth, _ = new_img.shape
    for x in range(heidth):
        for y in range(width):
            res = 0
            for z in range(3):
                res += img[y][x][z]
            new_img[y][x] = res / 3
    plt.imshow(new_img)
    plt.show()
    return (new_img)
