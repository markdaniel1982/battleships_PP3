import random

import sys,time

def delprint(text,delay_time):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(delay_time)


class PlayArea:
    def __init__(self, board):
        self.board = board

    def get_let_to_num():
        let_to_num = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}
        return let_to_num

# CODE CREDIT - https://stackoverflow.com/questions/35401019
# /how-do-i-print-something-underlined-in-python
    def print_board(self):
        print("\u0332".join("  A B C D E"))
        row_number = 1
        for row in self.board:
            print("%d|%s|" % (row_number, "|".join(row)))
            row_number += 1


class Battleship:
    def __init__(self, board):
        self.board = board

    def place_ships(self):
        for i in range(5):
            self.Xrow, self.Yclm = random.randint(
                0, 4), random.randint(0, 4)
            while self.board[self.Xrow][self.Yclm] == "X":
                self.Xrow, self.Yclm = random.randint(
                    0, 4), random.randint(0, 4)
            self.board[self.Xrow][self.Yclm] = "X"
        return self.board

    def get_user_input(self):
        try:
            Xrow = input("Choose a row (1-5): ")
            while Xrow not in "12345":
                print("Not a valid choice. Please select a valid row")
                Xrow = input("Choose a row (1-5): ")

            Yclm = input("Choose a column (a-e): ").upper()
            while Yclm not in "ABCDE":
                print("Not a valid choice. Please select a valid column")
                Yclm = input("Choose a column (a-e): ").upper()
            return int(Xrow) - 1, PlayArea.get_let_to_num()[Yclm]
        except ValueError and KeyError:
            print("Not a valid input")
            return self.get_user_input()

    def count_hit_ships(self):
        hit_ships = 0
        for row in self.board:
            for column in row:
                if column == "X":
                    hit_ships += 1
        return hit_ships


def RunGame():
    user_name = input("Please enter your name: ")
# CODE CREDIT Rules question - https://bobbyhadz.com/blog/python-input-yes-no
    yes_choices = ['yes', 'y']
    no_choices = ['no', 'n']

    def show_rules():
        delprint("\nFirst, select a row number between 1 & 5\n",.05)
        delprint("Then select a column letter between A & E\n",.05)
        delprint("if you hit a ship, an X will appear\n",.05)
        delprint("if you miss, a - will appear\n\n",.05)
        delprint(f"Ready {user_name}. Let's Play!\n\n", .05)

    while True:
        user_input = input('Do you want to see the rules? (yes/no): ')
        if user_input.lower() in yes_choices:
            show_rules()
            break
        elif user_input.lower() in no_choices:
            delprint(f"OK {user_name}. Let's play!\n", .05)
            break
        else:
            print('Type yes or no')
            continue

    computer_board = PlayArea([[" "] * 5 for i in range(5)])
    usrbd = PlayArea([[" "] * 5 for i in range(5)])
    Battleship.place_ships(computer_board)

    turns = 10
    while turns > 0:
        PlayArea.print_board(usrbd)
        Xrow, Yclm = Battleship.get_user_input(object)
        while usrbd.board[Xrow][Yclm] == "-" or usrbd.board[Xrow][Yclm] == "X":
            print("You've already guessed that. Please make another selection")
            Xrow, Yclm = Battleship. get_user_input(object)
        if computer_board.board[Xrow][Yclm] == "X":
            print(f"{user_name} sunk 1 of the Battleships!")
            usrbd.board[Xrow][Yclm] = "X"
        else:
            print("You Missed!")
            usrbd.board[Xrow][Yclm] = "-"
        if Battleship.count_hit_ships(usrbd) == 5:
            print(f"{user_name} hit all 5 battleships. WINNER!")
            break

        turns -= 1
        print(f"you have {turns} tries remaining")
        if turns == 0:
            print(f"Sorry {user_name}, you ran out of tries. Game Over")
            PlayArea.print_board(usrbd)
            break



RunGame()
