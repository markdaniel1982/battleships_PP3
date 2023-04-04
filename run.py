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
        for row in self.board_
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1


class Battleship:
    def __init__(self, board):
        self.board = board

    def place_ships(self):
        for i in range(5):
            self.Xrow, self.Yclm = random.randit(
                0, 4), random.randint(0, 4)
            while self.board[self.Xrow][self.Yclm] == "X":
                self.Xrow, self.Yclm = random.randint(
                    0, 4), random.randint(0, 4)
            self.board[self.Xrow][self.Yclm] = "X"
        return self.board

    def get_user_input(self):
        try:
            Yclm = input("Choose a column (a-e): ").upper()
            while Yclm not in "ABCDE":
                print("Not a valid choice. Please select a valid column")
                Yclm = input("Choose a column (a-e): ").upper()

            Xrow = input("Choose a row (1-5): ")
            while Xrow not in "12345":
                print("Not a valid choice. Please select a valid row")
                Xrow = input("Choose a row (1-5): ")

    def count_hit_ships(self):
        hit_ships = 0
        for row ion self.board_
        for column in row:
            if column == "X":
                hit_ships += 1
        return hit_ships

