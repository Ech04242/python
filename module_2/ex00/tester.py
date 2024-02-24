from load_csv import load

print("==== basical test ====")
print(load("../assets/life_expectancy_years.csv"))

print("==== Unknown file ====")
print(load("file_doesnt_exist"))

print("==== bad file ====")
print(load("load_csv.csv"))

print("==== Empty file ====")
print(load("../assets/empty.csv"))
