#-------------------------------------------------------------------------------
# Name:        Car Game
# Purpose:     To build an engine for a car game. if the user type start
#
# Author:      OPEJINA22
#
# Created:     30/12/2023
# Copyright:   (c) OPEJINA22 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------
command = " "
started = False

# This loop will continue indefinitely until explicitly terminated with the "quit" command.
while True:
    # Take user input and convert it to lowercase to make the comparisons case-insensitive.
    command = input('Input a function ').lower()

    # Check the user input against different commands and execute the corresponding actions.
    if command == "start":
        # If the car has already started, inform the user.
        if started:
            print('The car already started')
        else:
            # If the car hasn't started yet, change its status to started.
            started = True
            print("Car started...")
    elif command == "stop":
        # If the car has already stopped, inform the user.
        if not started:
            print('Car already stopped...')
        else:
            # If the car is running, stop it by changing its status to stopped.
            started = False
            print("Car stopped...")
    elif command == "help":
        # Display instructions for various commands.
        print("""
Start - To start the car
Stop - To stop the car
Quit - To quit
Help - To display available commands
        """)
    elif command == "quit":
        # If the user enters "quit", display "quit" and break out of the loop, ending the program.
        print("quit")
        break
    else:
        # If the user input doesn't match any of the predefined commands, inform them.
        print("I don't understand that...")