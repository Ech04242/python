def NULL_not_found(obj):
    if obj is None:
        print(f"Nothing: {obj} {type(obj)}")
    elif isinstance(obj, bool):
        print(f"Fake: {obj} {type(obj)}")
    elif isinstance(obj, int):
        print(f"Zero: {obj} {type(obj)}")
    elif isinstance(obj, float) and str(obj).lower() == 'nan':
        print(f"Cheese: {obj} {type(obj)}")
    elif isinstance(obj, str) and obj.lower() == '':
        print(f"Empty: {obj}{type(obj)}")
    else:
        print("Type not Found")
    return 1;
