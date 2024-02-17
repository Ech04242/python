from load_image import ft_load
import numpy as np

if __name__ == "__main__":

    img = ft_load("../assets/animal.jpeg")
    if img is None:
        exit()
    print(img)
    new_img = np.array([img[0], img[0]])
    print("New shape after slicing: ", np.array(new_img).shape)
