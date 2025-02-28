inp = input("Enter a var to check its value: ")

dict = {
    "1": "Hello",
    "2": "World",
    "3": "Meiw",
    "4": "Bruh",
    "5": "Niga",
}

if inp in dict.keys():
    print(f"{inp}: {dict[inp]}")
else:
    print("no such key found")