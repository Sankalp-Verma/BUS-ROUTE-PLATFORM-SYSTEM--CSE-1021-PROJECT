# System Design

## System Architecture

```text
              User
                |
                v
             main.py
             /     \
            v       v
   bus_functions   platform_checker
            |             |
            v             v
         bus_data.py <----+
User
 |
 +--> View Available Buses
 |
 +--> Check Bus Platform
 |
 +--> View Bus Details
 |
 +--> Exit Program
 main.py
  |
  +--> bus_functions.py
  |       |
  |       +--> bus_data.py
  |
  +--> platform_checker.py
          |
          +--> bus_functions.py
User -> main.py: Select option
main.py -> bus_functions.py: Request bus information
bus_functions.py -> bus_data.py: Read bus data
bus_data.py -> bus_functions.py: Return data
bus_functions.py -> main.py: Return result
main.py -> User: Display result
