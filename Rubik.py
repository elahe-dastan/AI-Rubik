from Side import Side


class Rubik:
    path_cost = 0

    def __init__(self, sides_list):
        self.sides_list = sides_list

    def right_rotation(self, side_number):
        if side_number == 1:
            self.first_side_right_rotation()
        if side_number == 2:
            self.second_side_right_rotation()
        if side_number == 3:
            self.third_side_right_rotation()
        if side_number == 4:
            self.left_rotation(2)
        if side_number == 5:
            self.left_rotation(1)
        if side_number == 6:
            self.left_rotation(3)

    def left_rotation(self, side_number):
        for i in range(3):
            self.right_rotation(side_number)

    def first_side_right_rotation(self):
        first_side = self.sides_list[0]
        first_side.right_rotation()
        tmp1 = self.sides_list[5].cells[3]
        tmp2 = self.sides_list[5].cells[2]
        self.sides_list[5].cells[2:4] = self.sides_list[1].cells[::-1][2:4]
        self.sides_list[1].cells[0:2] = self.sides_list[2].cells[0:2]
        self.sides_list[2].cells[0:2] = self.sides_list[3].cells[0:2]
        self.sides_list[3].cells[0] = tmp1
        self.sides_list[3].cells[1] = tmp2
        print("side one turned right")

    def second_side_right_rotation(self):
        second_side = self.sides_list[1]
        second_side.right_rotation()
        tmp1 = self.sides_list[5].cells[2]
        tmp2 = self.sides_list[5].cells[0]
        self.sides_list[5].cells[2] = self.sides_list[4].cells[2]
        self.sides_list[5].cells[0] = self.sides_list[4].cells[0]
        self.sides_list[4].cells[2] = self.sides_list[2].cells[2]
        self.sides_list[4].cells[0] = self.sides_list[2].cells[0]
        self.sides_list[2].cells[2] = self.sides_list[0].cells[2]
        self.sides_list[2].cells[0] = self.sides_list[0].cells[0]
        self.sides_list[0].cells[2] = tmp1
        self.sides_list[0].cells[0] = tmp2
        print("side two turned right")

    def third_side_right_rotation(self):
        third_side = self.sides_list[2]
        third_side.right_rotation()
        tmp1 = self.sides_list[4].cells[0]
        tmp2 = self.sides_list[4].cells[1]
        self.sides_list[4].cells[0] = self.sides_list[3].cells[2]
        self.sides_list[4].cells[1] = self.sides_list[3].cells[0]
        self.sides_list[3].cells[2] = self.sides_list[0].cells[3]
        self.sides_list[3].cells[0] = self.sides_list[0].cells[2]
        self.sides_list[0].cells[3] = self.sides_list[1].cells[1]
        self.sides_list[0].cells[2] = self.sides_list[1].cells[3]
        self.sides_list[1].cells[1] = tmp1
        self.sides_list[1].cells[3] = tmp2
        print("side three turned right")

    def print_rubik(self):
        for side in self.sides_list:
            side.print_side()

    def children_nodes(self):
        children_list = []
        for side_number in range(1, len(self.sides_list)+1):
            child_rubik = self.copy_rubik()
            child_rubik.right_rotation(side_number)
            children_list.append(child_rubik)

        for side_number in range(1, len(self.sides_list)+1):
            child_rubik = self.copy_rubik()
            child_rubik.left_rotation(side_number)
            children_list.append(child_rubik)

        return children_list

    def copy_rubik(self):
        sides_list_copy = []
        for i in range(len(self.sides_list)):
            side_copy = Side(self.sides_list[i].cells.copy())
            sides_list_copy.append(side_copy)
        return Rubik(sides_list_copy)

    def equal(self, rubik):
        for side_number in range(len(self.sides_list)):
            for cell_number in range(len(self.sides_list[side_number].cells)):
                if self.sides_list[side_number].cells[cell_number] != rubik.sides_list[side_number].cells[cell_number]:
                    return False
        return True



