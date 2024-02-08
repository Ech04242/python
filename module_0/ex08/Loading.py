from time import time


def ft_tqdm(list):
    """_summary_
        this function write an loading bar
    Args:
        list (_type_): list with element to it
    Yields:
        _type_: keep last config all time of function is called
    """
    if (not list):
        print("0it [00:00, ?it/s]")
        return
    start = time()
    maxValue = max(list) + 1
    len = 169
    now = 0
    for i in list:
        per = int(i / maxValue * 100) + 1 if maxValue else 0
        barLen = int(len * (per / 100)) if i else 0
        speed = 1 / (time() - now - start)
        remTime = int((maxValue - i) / speed)
        now = time() - start
        min = int(now / 60)
        sec = int(now % 60)
        minR = int(remTime / 60)
        secR = int(remTime % 60)
        print(f"\r{per:3d}%|", end="")
        print("█" * barLen, end="")
        print(" " * (len - barLen), end="| ")
        print(f"{i + 1}/{maxValue}", end=" [")
        print(f"{min:02d}:{sec:02d}<{minR:02d}:{secR:02d}", end=", ")
        print(round(speed, 2), end="it/s]")
        yield i
