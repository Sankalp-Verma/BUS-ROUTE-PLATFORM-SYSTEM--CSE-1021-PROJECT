from .bus_data import buses


def show_Buses():
    print("Available Buses")

    for bus in buses:
        print(bus, "-", buses[bus]["destination"])


def find_Platform(bus):
    if bus in buses:
        return buses[bus]["platform"]
    else:
        return 0


def find_Destination(bus):
    if bus in buses:
        return buses[bus]["destination"]
    else:
        return "Not Available"


def bus_Details(bus):
    platform = find_Platform(bus)
    destination = find_Destination(bus)

    if platform == 0:
        print("Bus not found.")
    else:
        print("Bus Details")
        print("Bus Number :", bus)
        print("Destination :", destination)
        print("Platform :", platform)