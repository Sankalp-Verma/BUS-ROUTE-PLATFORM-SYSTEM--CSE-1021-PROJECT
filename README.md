# Bus Route & Platform System

## Overview

The Bus Route & Platform System is a Python-based menu-driven application that provides basic bus route and platform information.

The system allows users to view available buses, check the correct platform for a bus, and view complete bus details.

## Features

- View available buses and destinations.
- Check the platform assigned to a bus.
- Verify whether a bus is at a particular platform.
- View bus details including bus number, destination, and platform.
- Handle invalid bus numbers.
- Provide a simple menu-driven interface.

## Technologies and Tools

- Python
- Visual Studio Code
- GitHub
## Project Structure

```text
Bus-Route-Platform-System
├── src
│   ├── __init__.py
│   ├── bus_data.py
│   ├── bus_functions.py
│   ├── main.py
│   └── platform_checker.py
├── tests
│   └── test_bus.py
├── docs
│   └── workflow.md
├── README.md
└── statement.md
```
## How to Run

Open the terminal in the main project folder and run:

```bash
python -m src.main
```
## Testing

Run the tests using:
```bash
python -m pytest
```
The tests check bus platforms, destinations, and invalid bus numbers.
