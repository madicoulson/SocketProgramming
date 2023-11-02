"""
CS 4065 - Computer Networks and Networked Computing
University of Cincinnati - Fall 2023
Project #2: Bulletin Board
Project Team: Preston Buterbaugh, Madilyn Coulson, Chloe Belletti
Bulletin Board Client
"""

import sys


def main() -> int:
    """
    @brief  This is the main function for the Bulletin Board Client
    @return: (int) Whether the client exited with an error
    """
    # Print menu options
    print('Bulletin Board Client Options: ')
    print('connect [server address] [server connection port] - Connects to a bulletin board server')
    print('join - Joins the message board on the connected server')
    print('post [subject] [message text] - Posts a message on the bulletin board')
    print('users - Lists the users currently on the message board')
    print('leave - Leaves the message board')
    print('message [message ID] - Gets the content of a message')
    print('exit - Leaves the message board (if applicable) and exits the client program')

    # Set current command
    command = ''

    # Loop until command is "exit"
    while command != 'exit':

        # Get next command
        command = input()

        # Check command
        if command == 'exit':
            print('Exiting')
            return 0
        elif command.startswith('connect ') or command.startswith('post ') or command.startswith('message ') or command == 'join' or command == 'users' or command == 'leave':
            print('This command is not yet implemented')
        else:
            print('Invalid command')


if __name__ == "__main__":
    sys.exit(main())