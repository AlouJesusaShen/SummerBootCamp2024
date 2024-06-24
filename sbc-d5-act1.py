office = []

while True:
    command = input("Command: ").strip().lower()
    if command.startswith("add"):
        item = command[3:].strip()
        if item:
            office.append(item)
        else:
            print("Please provide an item to add.")
    elif command.startswith("display"):
        print(office)
    
    elif command.startswith("naa"):
        if office:
            removed_item = office.pop(0)
            print(f"Removed item: {removed_item}")
        else:
            print("Office list is empty.")
    
    elif command.startswith("wala"):
        if office:
            removed_item = office.pop()
            print(f"Removed item: {removed_item}")
        else:
            print("Office list is empty.")
    else:
        print("Command Invalid")