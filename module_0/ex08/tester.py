from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm

if __name__ == "__main__":
    for elem in ft_tqdm(range(5000)):
        sleep(0.005)
    print()
    for elem in tqdm(range(5000)):
        sleep(0.005)
    print()
