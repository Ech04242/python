import pandas as pd


def load(path: str):
    """ load an CSV file and return data

    Args:
        path (str): link to CSV

    Raises:
        TypeError / NameError : bad file link

    Returns:
        _type_: data of csv , None on error
    """
    try:
        if not isinstance(path, str):
            raise TypeError("path is not str type !")
        if not path.endswith(".csv"):
            raise NameError("file don t finished by .csv")
        data = pd.read_csv(path)
        print(f"Loading dataset of dimension {data.shape}")
        print(data)
        return data
    except Exception as error:
        print("Error: ", error)
        return None
