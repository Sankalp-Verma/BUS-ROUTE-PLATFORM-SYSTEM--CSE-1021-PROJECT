# Problem Statement

## Problem

Managing bus routes and platform information manually can be confusing, especially when multiple buses use different platforms. Users need a simple system to find a bus destination, check its assigned platform, and view its details.

## Scope

The Bus Route & Platform System provides basic bus information and platform checking through a simple menu-driven Python program.

## Target Users

The system is intended for students, passengers, and other users who need quick access to bus route and platform information.

## Objectives

1. Display available buses and their destinations.
2. Check the correct platform for a selected bus.
3. Display complete details of a selected bus.
4. Provide a simple and easy-to-use menu-driven interface.
## High-Level Features

- View all available buses and their destinations.
- Find the platform assigned to a bus.
- Check whether a bus is at the entered platform.
- View complete bus details.
- Handle invalid bus numbers and menu choices.
- Exit the program safely.

## Technologies Used

- Python
- Visual Studio Code
- GitHub

## Project Structure

The project is divided into separate modules for better organization and maintainability. Bus data is stored separately, bus-related functions are handled in `bus_functions.py`, platform checking is handled in `platform_checker.py`, and `main.py` controls the main program flow.

## Non-Functional Requirements

### Performance
The system should provide bus information and platform results quickly.

### Usability
The system should have a simple menu-driven interface that is easy to understand and use.

### Reliability
The system should provide consistent results for valid bus numbers and platform checks.

### Maintainability
The program is divided into separate modules so that functions and data can be updated easily.

### Error Handling
The system should handle invalid bus numbers and invalid menu choices without crashing.
