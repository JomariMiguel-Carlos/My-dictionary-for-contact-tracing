print ("**********      PROGRAMMED BY      **********")
print ("**********  CARLOS, JOMARI MIGUEL  **********")
print ("**********        BSCOE 2-2        **********")
print ("********** Sir Danilo Madrigalejos **********")

details={}

def menu():
    print("\n-----------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("-----------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("Welcome to contact Tracing")
    print("1 -> Add contact")
    print("2 -> Search contact")
    print("3 -> Exit")

def exit():
    print("Thank you for using this code!")

while True:
    menu()
    choice = int(input("\nWhat do you want to do? "))

    if choice == 1:
        name = input("Enter name: ")
        loc = input("Where are you from?: ")
        try:
            age = int(input("Enter age: "))
            phone = int(input("Enter contact number: "))
        except ValueError:
            print("Invalid, Try again")
        else:
            print("-----------------------------------------------------------------------------------------------------------------------------------------------------------")
            details[name] = {
                "Age: ": age,
                "Address: ": loc,
                "Contact number: ": phone
            }
            print("Saved! Here is your new contact tracing list...")
            print(details)


    elif choice == 2:
        find = input("Enter full name of your target name: ")
        if find in details:
            print("-----------------------------------------------------------------------------------------------------------------------------------------------------------")
            print("\nI've found out that", find, "is here in your list, here is the details...")
            for key, value in details[find].items():
                print(key,value)
        else:
            print(find,"is not on your list...")

    elif choice == 3:
        exit()
        break

    else:
        print("-----------------------------------------------------------------------------------------------------------------------------------------------------------")
        print("Invalid, try again")


    print("-----------------------------------------------------------------------------------------------------------------------------------------------------------")
    again = input("\nWould you like to try again the program? type y if yes, if no you can just press enter to end the program: ")
    if again == "y":
        continue
    else:
        print("-----------------------------------------------------------------------------------------------------------------------------------------------------------")
        print("Thank you for using the program!")
        break

