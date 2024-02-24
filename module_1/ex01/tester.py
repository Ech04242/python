from array2D import slice_me

print("===Basic tests===")
family = [[1.80, 78.4],
          [2.15, 102.7],
          [2.10, 98.5],
          [1.88, 75.2]]
print(slice_me(family, 0, 2))
print(slice_me(family, 1, -2))


print("=== bad start ===")
print(slice_me(family, "bad", 2))

print("=== bad end ===")
print(slice_me(family, 42, "bad"))

print("=== nothing on family ===")
family = []
print(slice_me(family, 42, 10))

print("=== bad array line ===")
family = [[1.80, 78.4],
          [2.15, 102.7, 42.42],
          [2.10, 98.5],
          [1.88, 75.2]]
print(slice_me(family, 0, 2))
