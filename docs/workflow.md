# System Workflow

The Bus Route & Platform System allows users to view available buses, check the platform of a bus, and view complete bus details.

## Workflow

1. The program starts from `main.py`.
2. The main menu is displayed to the user.
3. The user selects an option from the menu.
4. If the user selects **Show Available Buses**, the system displays all available buses and their destinations.
5. If the user selects **Check Bus Platform**, the user enters a bus number and platform number. The system checks whether the selected platform is correct.
6. If the user selects **Show Bus Details**, the user enters a bus number and the system displays its destination and platform.
7. If the user selects **Exit**, the program closes.
8. Invalid menu choices are handled by displaying an error message.

## Module Flow

```text
User
  |
  v
main.py
  |
  +----> bus_functions.py
  |          |
  |          +----> bus_data.py
  |
  +----> platform_checker.py
             |
             +----> bus_functions.py
Bus numbers, destinations, and platform numbers are stored in `bus_data.py`.

The functions in `bus_functions.py` retrieve the required bus information. `platform_checker.py` uses these functions to verify whether a bus is assigned to the entered platform.

The result is then displayed to the user through `main.py`.