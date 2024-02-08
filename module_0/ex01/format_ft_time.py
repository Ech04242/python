
from time import time, localtime, strftime

if __name__== "__main__":
    sec = time()
    print("Seconds since January 1, 1970: {:,.4f} or {:.2e} in scientific notation".format(sec, sec))
    sec = localtime()
    print (strftime("%b %d %Y", sec))
