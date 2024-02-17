import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """_summary_
        tronck an list
    Args:
        family (list): list with value to tronc
        start (int): line to start
        end (int): line for end
    Returns:
        list: _description_
    """
    try:
        if not isinstance(start, int) or not isinstance(end, int):
            raise ValueError("start or end is not integer")
        if not isinstance(family, list):
            raise ValueError("family is not list type")
        if not all(len(item) == len(family[0]) for item in family):
            raise AssertionError("array doesn t have same nb elem on lines")
        if not len(family):
            print("My shape is Empty")
            return []
        print("My shape is : ", np.array(family).shape)
        final = np.array(family[start:end])
        if not len(final):
            print("My new shape is : None")
        else:
            print("My new shape is : ", np.array(final).shape)
        return final
    except Exception as error:
        print("Error : ", error)
        return []
