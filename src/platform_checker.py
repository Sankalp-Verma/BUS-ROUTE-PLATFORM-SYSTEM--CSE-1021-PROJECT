from .bus_functions import find_Platform


def check_Bus(bus, platform):
    correct_Platform = find_Platform(bus)

    if correct_Platform == platform:
        return True
    else:
        return False


def check_Platform():
    bus = int(input("Enter bus number: "))

    if find_Platform(bus) == 0:
        print("Bus not found.")
    else:
        platform = int(input("Enter platform number: "))

        if check_Bus(bus, platform):
            print("Yes, the bus will come to Platform", platform)
        else:
            correct_Platform = find_Platform(bus)
            print("No, the bus will not come to Platform", platform)
            print("The bus will come to Platform", correct_Platform)