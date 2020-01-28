class Side:
    def __init__(self, cells_list):
        self.cells = cells_list

    def right_rotation(self):
        self.cells[0], self.cells[2], self.cells[3], self.cells[1] = self.cells[2], self.cells[3], self.cells[1], self.cells[0]

    def print_side(self):
        for j in self.cells:
            print(self.print_color(j), end=" ")
        print()

    def print_color(self, number):
        if number == 1:
            print("orange", end=" ")
        elif number == 2:
            print("green", end=" ")
        elif number == 3:
            print("white", end=" ")
        elif number == 4:
            print("blue", end=" ")
        elif number == 5:
            print("red", end=" ")
        elif number == 6:
            print("yellow", end=" ")
