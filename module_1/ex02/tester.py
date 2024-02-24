import sys
from load_image import ft_load

print("=== initial test ===")
if len(sys.argv) != 2:
    print("tester is python tester.py <PATH>")
else:
    print(ft_load(sys.argv[1]))

print("=== bad path type ===")
print(ft_load(-42))

print("=== empty path ===")
print(ft_load(""))

print("=== bad file ===")
print(ft_load("UnknownFile.jpg"))
