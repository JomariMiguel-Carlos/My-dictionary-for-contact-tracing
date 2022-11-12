print ("**********      PROGRAMMED BY      **********")
print ("**********  CARLOS, JOMARI MIGUEL  **********")
print ("**********        BSCOE 2-2        **********")
print ("********** Sir Danilo Madrigalejos **********")

details={}

def menu():
    print("\nWelcome to contact Tracing")
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
            details[name] = {
                "Age: ": age,
                "Address: ": loc,
                "Contact number: ": phone
            }
            print("Saved!")
            print(details)


    elif choice == 2:
        find = input("Enter full name of your target name: ")
        if find in details:
            print("\nI've found out that", find, "is here in your list")
            for key, value in details[find].items():
                print(key,value)
        else:
            print("Invalid")

    elif choice == 3:
        exit()
        break

    else:
        print("Invalid, try again")



