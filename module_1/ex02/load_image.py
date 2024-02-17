import matplotlib.pyplot as plt
import numpy as np


def ft_load(path: str) -> list:
    """_summary_
        load an picture and print his shape
    Args:
        path (str): link to picture

    Returns:
        list: content of image
        [] if error
    """
    try:
        if not isinstance(path, str):
            raise TypeError("path is not good type, need str")
        if not path:
            raise TypeError("path is Null")
        img = plt.imread(path)
        print("The shape of image is: ", np.array(img).shape)
        return img
    except Exception as error:
        print("Error :", error)
        return []
