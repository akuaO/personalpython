def pounds_kg_calculator():
    user_input = input("Type k if you want to convert from kilograms to pounds.\nType p if you want to convert from pounds to kilograms: ")
    if user_input == 'k' or "K":
        value = input("Enter value in kg: ")
        answer = float(value) * 2.205
        print(answer)
    elif user_input == 'p' or "P":
        value = input("Enter value in lbs: ")
        answer = float(value) / 2.205
        print(answer)
    else:
        print("Invalid value")

pounds_kg_calculator()
