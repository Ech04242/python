from give_bmi import give_bmi, apply_limit

print("====subject tests====")
height = [2.71, 1.15]
weight = [165.3, 38.4]
bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(apply_limit(bmi, 26))

print("=================")
print("||  GIVE_BMI   ||")
print("=================\n")

print("====bad len====")
height = [1]
weight = [1, 2]
bmi = give_bmi(height, weight)

print("====bad value====")
height = [1, -2]
weight = [1, 2]
bmi = give_bmi(height, weight)

print("==== No value ====")
height = []
weight = []
bmi = give_bmi(height, weight)
print(apply_limit(bmi, 42))

print("==== Bad type ====")
height = [1, 2, 3]
weight = [1, 2, "Hello World ! "]
bmi = give_bmi(height, weight)


print("=================")
print("|| APPLY_LIMIT ||")
print("=================\n")

print("=== No value ===")
bmi = []
print(apply_limit(bmi, 42))

print("=== Bad Value ===")
bmi = [12, 50, "hello !"]
print(apply_limit(bmi, 42))

print("=== min limit ===")
bmi = [12, 50, 0]
print(apply_limit(bmi, "test"))
