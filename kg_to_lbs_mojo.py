class Convert:  # class to store the functions

    def take_unit():  # function take the unit from the user
        unit = input("is your weight in Pounds(L) or kilograms(K): ")
        return unit

    def pound_to_kg(a):  # function to Convert from pounds to kg
        weight_kg = a*0.453592
        print(f"you are {weight_kg} Kg")
        return weight_kg

    def kg_to_pound(a):  # function to Convert from kg to pounds
        weight_pounds = a*2.20462
        print(f" you are { weight_pounds} Lbs")
        return weight_pounds


# variable to take and store the user input
weight = input("Enter your weight: ")
# function is called from the Convert class to take the unit
unit = Convert.take_unit()

while unit:
    if unit.upper() == "L":  # Convert to kg if the unit entered is pounds
        Convert.pound_to_kg(int(weight))
        break

    elif unit.upper() == "K":  # Convert to pounds if the unit entered is kg
        Convert.kg_to_pound(int(weight))
        break

    else:  # to loop back if the user enters a wrong unit
        print("please select the right conversion")
        unit = Convert.take_unit()
