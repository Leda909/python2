# Output to users
conversion_choice = input("Please, press '1' if you would like to convert pounds to kilograms, and press '2' if you want to convert kilograms to pounds: ")

# if user chooses pounds to kg
if conversion_choice == "1":
    pounds = float(input("How many pounds do you want to convert to kilogram? "))
    print("This is", pounds / 2.20462, "kg.")
# if user chooses kg to pounds
elif conversion_choice == "2":
    kilos = float(input("How many kilograms do you want to convert to pounds? "))
    print("This is", kilos * 2.20462, "pounds.")
# Error
else:
    print("No option chosen.")
