import pandas as pd


def load(path: str):
    try:
        if not isinstance(path, str):
            raise TypeError("path is not str type !")
        if not path.endswith(".csv"):
            raise NameError("file don t finished by .csv")
        data = pd.read_csv(path)
        return data
    except Exception as error:
        print("Error: ", error)
        return None
