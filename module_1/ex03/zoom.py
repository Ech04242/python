from load_image import ft_load
import matplotlib.pyplot as plt
import sys


if __name__ == "__main__":
    try:
        if len(sys.argv) < 2:
            raise ValueError("Bad numbers of argument, 1 is required")
        img = ft_load(sys.argv[1])
        if img is None:
            exit()
        print(img)
        img = img[100:500, 450:850, 0:1]
        print("New shape after slicing: ", img.shape)
        print(img)
        plt.imshow(img, cmap='gray')
        plt.show()
    except Exception as error:
        print("error: ", error)
