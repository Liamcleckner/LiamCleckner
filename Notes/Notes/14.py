empty_dict = {'stuff':42}

print(empty_dict)
empty_dict.clear()
print(f"now it's empty: {empty_dict}")

empty_dict['CO'] = "Denver"
empty_dict['WY'] = "Cheyenne"
empty_dict['UT'] = "SLC"
print(f"{empty_dict=}'")

if "CO" in empty_dict.keys():
    print("'CO' is in the dictionary.")

print(f"{empty_dict.keys()=}")
print(f"{empty_dict.values()=}")
print(f"{empty_dict.items()=}")

empty_dict['VT'] = "Montpelier"

if 'VT' in empty_dict:
    print(f"Value at 'VT': {empty_dict['VT']}")

if 'VT' in empty_dict.keys():
    print(f"Value at 'VT': {empty_dict['VT']}")

print(f"Value at 'VT': {empty_dict.get('VT', 'no se')}")