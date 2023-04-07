import random  #for creating ship positioning
import sys  # Used to add typing effect on display text
import time  # Used to add typing effect on display text

# CODE CREDIT - Main inspiration from
# https://www.youtube.com/watch?v=tF1WRCrd_HQ
# but heavily modified the code to suit this application

# CODE CREDIT - https://replit.com/talk/learn/The-Slow-Print/44741


def delPrint(text, delay_time):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(delay_time)


class PlayArea:
    """
    Create the game board and change column letters to numbers
    to allow hit/miss checks
    """
    def __init__(self, board):
        self.board = board

    def get_let_to_num():
        let_to_num = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}
        return let_to_num

# CODE CREDIT - https://stackoverflow.com/questions/35401019
# /how-do-i-print-something-underlined-in-python
    def printBoard(self):
        print("\u0332".join("  A B C D E"))
        row_number = 1
        for row in self.board:
            print("%d|%s|" % (row_number, "|".join(row)))
            row_number += 1


class Battleship:
    """    Create and place the ships on the board    """
    def __init__(self, board):
        self.board = board

# Xrow - Rows. Yclm - Columns. both shortened to fit
# within heroku deployment limits
    def placeShips(self):
        for i in range(5):
            self.Xrow, self.Yclm = random.randint(
                0, 4), random.randint(0, 4)
            while self.board[self.Xrow][self.Yclm] == "X":
                self.Xrow, self.Yclm = random.randint(
                    0, 4), random.randint(0, 4)
            self.board[self.Xrow][self.Yclm] = "X"
        return self.board

    def getUserInput(self):
        """        Recieve and validate input from user        """
        try:
            while True:
                Xrow = input("Choose a row (1-5): \n")
                if Xrow not in ["1", "2", "3", "4", "5"] or Xrow == "":
                    print("Not a valid choice. Please select a valid row")
                    continue
                else:
                    break
            while True:
                Yclm = input("Choose a column (A-E): \n").upper()
                if Yclm not in ["A", "B", "C", "D", "E"] or Yclm == "":
                    print("Not a valid choice. Please select a valid column")
                    continue
                else:
                    break
            return int(Xrow) - 1, PlayArea.get_let_to_num()[Yclm]
        except (ValueError, KeyError):
            print("Not a valid input")
            return self.getUserInput(self)

    def countHitShips(self):
        """        Calculate if hit/miss        """
        hit_ships = 0
        for row in self.board:
            for column in row:
                if column == "X":
                    hit_ships += 1
        return hit_ships


def runGame():

    # CREDIT - ASCII art from https://www.asciiart.eu/vehicles/navy
    print("""
Welcome to

                           _______/__/_
                  ___     /===========|   ___
 ____       __   [\\\]___/____________|__[///]   __
 \   \_____[\\]__/___________________________\__[//]___
  \  ___  ____ ___ ___ _    ____ ____ _  _ _ ___  ____ /
   \ |__] |__|  |   |  |    |___ [__  |__| | |__] |__ /
    \|__] |  |  |   |  |___ |___ ___] |  | | |    ___/
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")

    """
    Recieve users name and ask if they need to see rules/instructions
    and validates the responses
    """

    userName = input("Aye, Captain. What be your name?: \n")
    if userName == "":
        print("Please enter a name")
        userName = input("Aye, Captain. What be your name?: \n")

# CODE CREDIT Rules question - https://bobbyhadz.com/blog/python-input-yes-no
    yesChoices = ['yes', 'y']
    noChoices = ['no', 'n']

    def showRules():
        delPrint("\nFirst, select a row number between 1 & 5.\n", .03)
        delPrint("Then select a column letter between a & e.\n", .03)
        delPrint("If you hit a ship, an X will appear.\n", .03)
        delPrint("If you miss, a - will appear.\n\n", .03)
        delPrint(f"OK, Captain {userName}. Let's play!\n\n", .03)

    while True:
        userInput = input("Do you want to see the rules? (yes/no): \n")
        if userInput.lower() in yesChoices:
            showRules()
            break
        if userInput.lower() in noChoices:
            delPrint(f"OK, Captain {userName}. Let's play!\n\n", .03)
            break
        else:
            print('Type yes or no')
            continue

    computerBoard = PlayArea([[" "] * 5 for i in range(5)])
    usrbd = PlayArea([[" "] * 5 for i in range(5)])
    Battleship.placeShips(computerBoard)
    """    Counts down number of tries and validates guesses    """
    turns = 10
    while turns > 0:
        PlayArea.printBoard(usrbd)
        Xrow, Yclm = Battleship.getUserInput(object)
        while usrbd.board[Xrow][Yclm] == "-" or usrbd.board[Xrow][Yclm] == "X":
            print("\nYou've already guessed that. Make another selection\n")
            Xrow, Yclm = Battleship.getUserInput(object)
        if computerBoard.board[Xrow][Yclm] == "X":
            print(f"\n{userName} sunk 1 of the Battleships!\n")
            usrbd.board[Xrow][Yclm] = "X"
        else:
            print("\nYou Missed!\n")
            usrbd.board[Xrow][Yclm] = "-"
        if Battleship.countHitShips(usrbd) == 5:
            print(f"{userName} hit all 5 battleships. WINNER!\n")
            break
        """        Ends game if turns reaches 0        """
        turns -= 1
        print(f"you have {turns} tries remaining")
        if turns == 0:
            print(f"Sorry {userName}, you ran out of tries. Game Over\n")
            PlayArea.printBoard(usrbd)
            break


runGame()
