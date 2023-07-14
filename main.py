#Print/Display Heading for Program
print("=============================")
print("  Welcome to the UMBC Car")
print("Customization Selection Form")
print("=============================")

#Print Blank line to add space betweem next section
print()

#Print/Display list of cars to choice from
print("(For multiple choice questions, please enter the letter of the choice you want)")

#Print Blank line to add space betweem next section
print()

#Print/Display heading for Make & Model Section
print("~ Make & Model ~")

#Print/Display list of cars to choice from
print("Select your choice for Make and Model of car you want:")
print("1. Choose the Model of Car you want:")
print("    a. Acura MDX")
print("    b. Acura RDX")
print("    c. Audi A4")
print("    d. Audi A8")
print("    e. BMW 5 Series")
print("    f. BMW 7 Series")
print("    g. Cadillac ATS")
print("    h. Jaguar F-Type")
carChoice = input("Please enter one of the car choices from above (e.g.,'a' - 'h'): ")

#Print Blank line to add space betweem next section
print()

print("2. Would you like to upgrade from a 4-door option to a 2-door option?")

#Print Blank line to add space betweem next section
print()

upgradeChoice = input("Please enter 'yes' or 'no': ")

#Print Blank line to add space betweem next section
print()

#Print/Display heading for Exterior Section
print("~ Exterior ~")
print("3. What color would you like your car to have?")
colorChoice = input("Please enter the name of the color you'd like: ")

#Print Blank line to add space betweem next section
print()

#Print/Display deluxe weather package question
print("4. Would you like to the deluxe weather package?")
packageChoice = input("Please enter 'yes' or 'no': ")

#Print Blank line to add space betweem next section
print()

#Print/Display heading for Interior Section
print("~ Interior ~")

#Print/Display list of Engine Type question
print("5. Which Engine would you like your car to have?")
print("    a. I-4 Entry Engine")
print("    b. V-6 Performance Engine")
print("    c. V-8 High Performce Engine")
print("    d. Eco Diesel Engine")
print("    e. Hybrid Gas & Electrical Engine")
print("    f. All Electric Plug-in Engine")
engineChoice = input("Please enter one of the Engine choices from above (e.g.,'a' - 'f'): ")

#Print Blank line to add space betweem next section
print()

print("6. Would you like heated seats?")
seatChoice = input("Please enter 'yes' or 'no': ")

#Print Blank line to add space betweem next section
print()

#Print/Display Summary of Custom Car Selections
print("======================================")
print("            ~ Summary ~")
print("======================================")
print(f"Make & Model Option: {carChoice}")
print(f"Upgrade to 2-Door Option: {upgradeChoice}")
print(f"Desired Color Option: {colorChoice}")
print(f"Upgrade to Deluxe Weather Option: {packageChoice}")
print(f"Engine Option: {engineChoice}")
print(f"Upgrade to Heated Seats Option: {seatChoice}")
