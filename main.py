
# Ultimate Battleships

def print_ships_to_be_placed():
    print("Ships to be placed:", end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Ships to be placed: ")


# elem expected to be a single list element of a primitive type.
def print_single_element(elem):
    print(str(elem), end=" ")
    if FILE_OUTPUT_FLAG:
        f.write(str(elem) + " ")


def print_empty_line():
    print()
    if FILE_OUTPUT_FLAG:
        f.write("\n")


# n expected to be str or int.
def print_player_turn_to_place(n):
    print("It is Player {}'s turn to place their ships.".format(n))
    if FILE_OUTPUT_FLAG:
        f.write("It is Player {}'s turn to place their ships.\n".format(n))


def print_to_place_ships():
    print("Enter a name, coordinates and orientation to place a ship (Example: Carrier 1 5 h) :", end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Enter a name, coordinates and orientation to place a ship (Example: Carrier 1 5 h) : \n")
        # There is a \n because we want the board to start printing on the next line.


def print_incorrect_input_format():
    print("Input is in incorrect format, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write("Input is in incorrect format, please try again.\n")


def print_incorrect_coordinates():
    print("Incorrect coordinates given, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write("Incorrect coordinates given, please try again.\n")


def print_incorrect_ship_name():
    print("Incorrect ship name given, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write("Incorrect ship name given, please try again.\n")


def print_incorrect_orientation():
    print("Incorrect orientation given, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write("Incorrect orientation given, please try again.\n")


# ship expected to be str.
def print_ship_is_already_placed(ship):
    print(ship, "is already placed, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write(ship + " is already placed, please try again.\n")


# ship expected to be str.
def print_ship_cannot_be_placed_outside(ship):
    print(ship, "cannot be placed outside the board, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write(ship + " cannot be placed outside the board, please try again.\n")


# ship expected to be str.
def print_ship_cannot_be_placed_occupied(ship):
    print(ship, "cannot be placed to an already occupied space, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write(ship + " cannot be placed to an already occupied space, please try again.\n")


def print_confirm_placement():
    print("Confirm placement Y/N :", end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Confirm placement Y/N : \n")


# n expected to be str or int.
def print_player_turn_to_strike(n):
    print("It is Player {}'s turn to strike.".format(n))
    if FILE_OUTPUT_FLAG:
        f.write("It is Player {}'s turn to strike.\n".format(n))


def print_choose_target_coordinates():
    print("Choose target coordinates :", end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Choose target coordinates : ")


def print_miss():
    print("Miss.")
    if FILE_OUTPUT_FLAG:
        f.write("Miss.\n")


# n expected to be str or int.
def print_type_done_to_yield(n):
    print("Type done to yield your turn to player {} :".format(n), end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Type done to yield your turn to player {} : \n".format(n))


def print_tile_already_struck():
    print("That tile has already been struck. Choose another target.")
    if FILE_OUTPUT_FLAG:
        f.write("That tile has already been struck. Choose another target.\n")


def print_hit():
    print("Hit!")
    if FILE_OUTPUT_FLAG:
        f.write("Hit!\n")


# n expected to be str or int.
def print_player_won(n):
    print("Player {} has won!".format(n))
    if FILE_OUTPUT_FLAG:
        f.write("Player {} has won!\n".format(n))


def print_thanks_for_playing():
    print("Thanks for playing.")
    if FILE_OUTPUT_FLAG:
        f.write("Thanks for playing.\n")


# my_list expected to be a 3-dimensional list, formed from two 2-dimensional lists containing the boards of each player.
def print_3d_list(my_list):
    first_d = len(my_list[0])
    for row_ind in range(first_d):
        second_d = len(my_list[0][row_ind])
        print("{:<2}".format(row_ind+1), end=' ')
        for col_ind in range(second_d):
            print(my_list[0][row_ind][col_ind], end=' ')
        print("\t\t\t", end='')
        print("{:<2}".format(row_ind+1), end=' ')
        for col_ind in range(second_d):
            print(my_list[1][row_ind][col_ind], end=' ')
        print()
    print("", end='   ')
    for row_ind in range(first_d):
        print(row_ind + 1, end=' ')
    print("\t\t", end='   ')
    for row_ind in range(first_d):
        print(row_ind + 1, end=' ')
    print("\nPlayer 1\t\t\t\t\t\tPlayer 2")
    print()

    if FILE_OUTPUT_FLAG:
        first_d = len(my_list[0])
        for row_ind in range(first_d):
            second_d = len(my_list[0][row_ind])
            f.write("{:<2} ".format(row_ind + 1))
            for col_ind in range(second_d):
                f.write(my_list[0][row_ind][col_ind] + " ")
            f.write("\t\t\t")
            f.write("{:<2} ".format(row_ind + 1))
            for col_ind in range(second_d):
                f.write(my_list[1][row_ind][col_ind] + " ")
            f.write("\n")
        f.write("   ")
        for row_ind in range(first_d):
            f.write(str(row_ind + 1) + " ")
        f.write("\t\t   ")
        for row_ind in range(first_d):
            f.write(str(row_ind + 1) + " ")
        f.write("\nPlayer 1\t\t\t\t\t\tPlayer 2\n")
        f.write("\n")


def print_rules():
    print("Welcome to Ultimate Battleships")
    print("This is a game for 2 people, to be played on two 10x10 boards.")
    print("There are 5 ships in the game:  Carrier (occupies 5 spaces), Battleship (4), Cruiser (3), Submarine (3), and Destroyer (2).")
    print("First, the ships are placed. Ships can be placed on any unoccupied space on the board. The entire ship must be on board.")
    print("Write the ship's name, followed by an x y coordinate, and the orientation (v for vertical or h for horizontal) to place the ship.")
    print("If a player is placing a ship with horizontal orientation, they need to give the leftmost coordinate.")
    print("If a player is placing a ship with vertical orientation, they need to give the uppermost coordinate.")
    print("Player 1 places first, then Player 2 places. Afterwards, players take turns (starting from Player 1) to strike and sink enemy ships by guessing their location on the board.")
    print("Guesses are again x y coordinates. Do not look at the board when it is the other player's turn.")
    print("The last player to have an unsunk ship wins.")
    print("Have fun!")
    print()

    if FILE_OUTPUT_FLAG:
        f.write("Welcome to Ultimate Battleships\n")
        f.write("This is a game for 2 people, to be played on two 10x10 boards.\n")
        f.write(
            "There are 5 ships in the game:  Carrier (occupies 5 spaces), Battleship (4), Cruiser (3), Submarine (3), and Destroyer (2).\n")
        f.write(
            "First, the ships are placed. Ships can be placed on any unoccupied space on the board. The entire ship must be on board.\n")
        f.write(
            "Write the ship's name, followed by an x y coordinate, and the orientation (v for vertical or h for horizontal) to place the ship.\n")
        f.write("If a player is placing a ship with horizontal orientation, they need to give the leftmost coordinate.\n")
        f.write("If a player is placing a ship with vertical orientation, they need to give the uppermost coordinate.\n")
        f.write(
            "Player 1 places first, then Player 2 places. Afterwards, players take turns (starting from Player 1) to strike and sink enemy ships by guessing their location on the board.\n")
        f.write("Guesses are again x y coordinates. Do not look at the board when it is the other player's turn.\n")
        f.write("The last player to have an unsunk ship wins.\n")
        f.write("Have fun!\n")
        f.write("\n")


# Create the game
board_size = 10
f = open('UltimateBattleships.txt', 'w')
FILE_OUTPUT_FLAG = True  # You can change this to True to also output to a file so that you can check your outputs with diff.

print_rules()

# Remember to use list comprehensions at all possible times.
# If we see you populate a list that could be done with list comprehensions using for loops, append/extend/insert etc. you will lose points.

# Make sure to put comments in your code explaining your approach and the execution.

# We defined all the functions above for your use so that you can focus only on your code and not the formatting.
# You need to call them in your code to use them of course.

# If you have questions related to this homework, direct them to utku.bozdogan@boun.edu.tr please.

# Do not wait until the last day or two to start doing this homework, it requires serious effort.

try:  # The entire code is in this try block, if there ever is an error during execution, we can safely close the file.
    # DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
    #First, I defined some useful lists and dicts for later use.
    lst = ["Carrier", "Battleship", "Cruiser", "Submarine", "Destroyer"]
    lst_Untouched=["carrier", "battleship", "cruiser", "submarine", "destroyer"]
    dct = {"carrier": 5, "battleship": 4, "cruiser": 3, "submarine": 3, "destroyer": 2}
    my_list=[[["-" for i in range(10)] for j in range(10)] for k in range(2)]
    The_board_of_player_1=[]
    The_board_of_player_2=[]
    #There are 2 players,so each must have a distinct board.
    for player in range(2):
        while True:
            print_3d_list(my_list)
            print_ships_to_be_placed()
            for elem in lst:
                print_single_element(elem)
            print_empty_line()
            print_player_turn_to_place(player+1)
            print_to_place_ships()
            #I lowered capital letters to work on them easily
            lower_lst=[i.lower() for i in lst]
            orientation_order=input()
            order_list=orientation_order.split()
            order_list[0]=order_list[0].lower()
            #Input format errors
            if len(order_list)>4:
                order_list=order_list[:4]
            if len(order_list)<4:
                print_incorrect_input_format()
                continue
            if not (order_list[1].isdigit() and order_list[2].isdigit()):
                print_incorrect_input_format()
                continue
            #Coordinate errors
            if int(order_list[1])<1 or int(order_list[1])>10 or int(order_list[2])<1 or int(order_list[2])>10:
                print_incorrect_coordinates()
                continue
            #Ship name errors(either inappropriate shipnames or already used ones)
            if not order_list[0] in lower_lst:
                if order_list[0] in lst_Untouched:
                    print_ship_is_already_placed(order_list[0][0].upper()+order_list[0][1:])
                    continue
                else:
                    print_incorrect_ship_name()
                    continue
            #Orientation errors
            if order_list[3].lower() != "v" and order_list[3].lower() != "h":
                print_incorrect_orientation()
                continue
            #I found the index of ship, so i can reach it on my dictionary
            ind=lower_lst.index(order_list[0])
            #Ship placement for Horizontal case
            if order_list[3]== "h" or order_list[3]== "H":
                #horizontal placement errors like placing outside
                if int(order_list[1])-1+dct[lower_lst[ind]]>10:
                    print_ship_cannot_be_placed_outside(order_list[0][0].upper()+order_list[0][1:])
                    continue
                #Coincidence errors for horizontal case
                coincidence_checker_horizontal=False
                for i in range(dct[lower_lst[ind]]):
                    if my_list[player][int(order_list[2])-1][int(order_list[1])+i-1]=="#":
                        coincidence_checker_horizontal=True
                        break
                if coincidence_checker_horizontal is True:
                    print_ship_cannot_be_placed_occupied(order_list[0][0].upper()+order_list[0][1:])
                    continue
                #Horizontal ship placement
                for i in range(dct[lower_lst[ind]]):
                    my_list[player][int(order_list[2])-1][int(order_list[1])+i-1]="#"
            #Vertical ship placement case
            if order_list[3]== "v" or order_list[3]== "V":
                # vertical placement errors like placing outside
                if int(order_list[2])-1+dct[lower_lst[ind]]>10:
                    print_ship_cannot_be_placed_outside(order_list[0][0].upper() + order_list[0][1:])
                    continue
                # Coincidence errors for vertical case
                coincidence_checker_vertical = False
                for j in range(dct[lower_lst[ind]]):
                    if my_list[player][int(order_list[2])-1+j][int(order_list[1])-1] == "#":
                        coincidence_checker_vertical = True
                        break
                if coincidence_checker_vertical is True:
                    print_ship_cannot_be_placed_occupied(order_list[0][0].upper() + order_list[0][1:])
                    continue
                # Vertical ship placement
                for j in range(dct[lower_lst[ind]]):
                    my_list[player][int(order_list[2])-1+j][int(order_list[1])-1]="#"
            #disposal of already placed ships and recreating ship name list in proper way(capitalizing first letter)
            lower_lst.remove(order_list[0].lower())
            lst=[i[0].upper()+i[1:] for i in lower_lst]
            #end of the placement
            if len(lst)==0:
                print_3d_list(my_list)
                while True:
                    print_confirm_placement()
                    answer=input()
                    if answer=="y" or answer=="Y" or answer=="n" or answer=="N":
                        break
                #if the player is happy with its board, then I take its board into another list and recreate my lists for the next player
                if answer == "Y" or answer == "y":
                    if player==0:
                        The_board_of_player_1 = my_list
                    if player==1:
                        The_board_of_player_2 = my_list
                    my_list = [[["-" for i in range(10)] for j in range(10)] for k in range(2)]
                    lst = ["Carrier", "Battleship", "Cruiser", "Submarine", "Destroyer"]
                    break
                # if the player is not happy with its board, then I recreate my lists and ask the same questions.
                if answer == "N" or answer == "n":
                    my_list = [[["-" for i in range(10)] for j in range(10)] for k in range(2)]
                    lst = ["Carrier", "Battleship", "Cruiser", "Submarine", "Destroyer"]
                    continue
    #The battle part begins here, and I defined a dictionary to keep the numbers of hits of two players.
    #Whoever reaches 17 hits first will win
    who_is_the_winner=dict()
    #this checker will be useful when getting out of the loops
    winner_check=True
    while True:
        if winner_check == False:
            break
        for player in range(2):
            if winner_check == False:
                break
            #I made a list of boards to call those boards with their indexes that I reach by player variable
            board_list=[The_board_of_player_1,The_board_of_player_2]
            while True:
                print_3d_list(board_list[player])
                print_player_turn_to_strike(player+1)
                print_choose_target_coordinates()
                target_coordinates=input()
                target_lst=target_coordinates.split()
                #incorrect input format errors
                if len(target_lst)>2:
                    target_lst=target_lst[:2]
                if len(target_lst)<2:
                    print_incorrect_input_format()
                    continue
                if not (target_lst[0].isdigit() and target_lst[1].isdigit()):
                    print_incorrect_input_format()
                    continue
                #incorrect coordinates errors
                if int(target_lst[0])<1 or int(target_lst[0])>10 or int(target_lst[1])>10 or int(target_lst[1])<1:
                    print_incorrect_coordinates()
                    continue
                #Trying to hit one place two times errors
                if board_list[1-player][1-player][int(target_lst[1])-1][int(target_lst[0])-1]=="O" or board_list[1-player][1-player][int(target_lst[1])-1][int(target_lst[0])-1]=="!":
                    print_tile_already_struck()
                    continue
                #For both player, hitting or missing. Thanks to the player variable, I do not have to write two case seperately.
                if board_list[1-player][1-player][int(target_lst[1])-1][int(target_lst[0])-1]=="-":
                    print_miss()
                    board_list[1-player][1-player][int(target_lst[1])-1][int(target_lst[0])-1]="O"
                    board_list[player][1-player][int(target_lst[1])-1][int(target_lst[0])-1]="O"
                    #try until get "done"
                    while True:
                        print_type_done_to_yield(2-player)
                        done=input()
                        if done.lower()=="done":
                            break
                    break
                if board_list[1-player][1-player][int(target_lst[1])-1][int(target_lst[0])-1]=="#":
                    print_hit()
                    board_list[1-player][1-player][int(target_lst[1])-1][int(target_lst[0])-1]="!"
                    board_list[player][1-player][int(target_lst[1])-1][int(target_lst[0])-1]="!"
                    #this is where I count the number of hits for both of the players,which then will be kept in my dictionary
                    who_is_the_winner[player]=who_is_the_winner.get(player,0)+1
                    #If one of the players reach 17 hits,which means the player has shot all the ships,then the game ends.
                    if who_is_the_winner[player] == 17:
                        print_3d_list(board_list[player])
                        print_player_won(player + 1)
                        #this checker will be useful when getting out of the loops
                        winner_check = False
                        break
                    continue
    print_thanks_for_playing()

    # DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
except:
    f.close()
