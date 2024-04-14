#when the game is started

# if the user inputs help it should give the list of game commands

# when the user enters start it prints "Car started...Ready to go"
# when the user enters stop it prints "car stopped"

# the user can still enter start for it to print "car started... ready to go"

# but when the user enters "quit" it exits the game



def car_game():
    while True:
        user_input = input("Type 'start' to start the car, 'stop' to stop the car, 'quit' to exit game and 'help' for game options: ")
        new_input = user_input.lower()
        if new_input == 'help':
            print("start - to start car\nstop - to stop car\nquit - to exit")
        elif new_input == 'start':
            print("Car started...Ready to go")
        elif new_input == 'stop':
            print("car_stopped")
        elif new_input == "quit":
            break
        else:
            print("Invalid command. Can't you follow instructions?")

car_game()








