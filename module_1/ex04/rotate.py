from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np
import sys


def transpose_img(img: list) -> list:
    """ transpose an picture to 90 degre

    Args:
        img (list): img to transpose

    Raises:
        ValueError: _description_

    Returns:
        list: new picture with transpose
    """
    try:
        width = img.shape[0]
        heidth = img.shape[1]
        new_img = np.zeros((heidth, width))
        for x in range(heidth):
            for y in range(width):
                new_img[y][x] = img[x][y][0]
        return (new_img)
    except Exception as error:
        print("error: ", error)
        return (None)


if __name__ == "__main__":
    try:
        if len(sys.argv) < 2:
            raise ValueError("Bad numbers of argument, 1 is required")
        img = ft_load(sys.argv[1])
        if img is None:
            exit()
        img = img[100:500, 450:850, 0:1]
        print("The shape of image is: ", img.shape)
        print(img)
        img = transpose_img(img)
        if img is None:
            exit()
        plt.imshow(img, cmap='gray')
        print("New shape after Transpose: ", img.shape)
        print(img)
        plt.show()
    except Exception as error:
        print("error: ", error)
