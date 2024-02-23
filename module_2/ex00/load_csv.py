import pandas as pd


def load(path: str):
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
