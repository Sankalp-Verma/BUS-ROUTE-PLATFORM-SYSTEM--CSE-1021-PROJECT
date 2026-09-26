from .bus_functions import show_Buses, bus_Details
from .platform_checker import check_Platform


def main():
    print("Bus Route & Platform System")

    while True:
        print("1. Show available buses")
        print("2. Check bus platform")
        print("3. Show bus details")
        print("4. Exit")

        choice = int(input("Enter Your Choice : "))

        if choice == 1:
            show_Buses()

        elif choice == 2:
            check_Platform()

        elif choice == 3:
            bus = int(input("Enter Bus Number : "))
            bus_Details(bus)

        elif choice == 4:
            print("Program closed.")
            break

        else:
            print("Invalid choice, Please try again.")


main()