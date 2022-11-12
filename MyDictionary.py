print ("**********      PROGRAMMED BY      **********")
print ("**********  CARLOS, JOMARI MIGUEL  **********")
print ("**********        BSCOE 2-2        **********")
print ("********** Sir Danilo Madrigalejos **********")

details={}

print (details.keys())
def menu():
    print("Welcome to contact Tracing")
    print("1 -> Add contact")
    print("2 -> Search contact")
    print("3 -> Exit (y/n)")

def exit():
    print("Thank you for using this code!")

while True:
    menu()
    choice = int(input("\n What do you want to do?"))

    if choice == 1:
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        loc = input("Where are you from?: ")
        phone = int(input("Enter contact number: "))
        details=[[name],[age],[loc],[phone]]
        details.append([[name],[age],[loc],[phone]])
        print(details)

    elif choice == 2:
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        loc = input("Where are you from?: ")
        phone = int(input("Enter contact number: "))
        details[roll] = [[name], [age], [loc], [phone]]

    elif choice == 3:
        print("Thank you for using this program!")
        exit()
        break

    else:
        print("Invalid, try again")