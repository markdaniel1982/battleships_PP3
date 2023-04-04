import random


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
    print(f"Welcome {user_name}. Let's play!")

    computer_board = PlayArea([[" "] * 5 for i in range(5)])
    user_board = PlayArea([[" "] * 5 for i in range(5)])
    Battleship.place_ships(computer_board)

    turns = 10
    while turns > 0:
        PlayArea.print_board(user_board)
        Xrow, Yclm = Battleship.get_user_input(object)
        while user_board.board[Xrow][Yclm] == "-" or user_board.board[Xrow][Yclm] == "X":
            print("You've already guessed that one. Please make another selection")
            Xrow, Yclm = Battleship. get_user_input(object)
        if computer_board.board[Xrow][Yclm] == "X":
            print(f"{user_name} sunk 1 of the Battleships!")
            user_board.board[Xrow][Yclm] = "X"
        else:
            print("You Missed!")
            user_board.board[Xrow][Yclm] = "-"
        if Battleship.count_hit_ships(user_board) == 5:
            print(f"{user_name} hit all 5 battleships. WINNER!")
            break

        turns -= 1
        print(f"you have {turns} tries remaining")
        if turns == 0:
            print(f"Sorry {user_name}, you ran out of tries. Game Over")
            PlayArea.print_board(user_board)
            break


RunGame()
