from Algorithm import Algorithm
from Rubik import Rubik
from Side import Side


def other_side_color(side_color):
    if side_color == 1:
        return 5
    elif side_color == 2:
        return 4
    elif side_color == 3:
        return 6
    elif side_color == 4:
        return 2
    elif side_color == 5:
        return 1
    elif side_color == 6:
        return 3


class Bidirectional(Algorithm):
    forward_queue = []
    backward_queue = []

    def __init__(self, initial_node):
        super().__init__()
        self.initial_node = initial_node
        self.goal_node = self.find_goal_state()
        self.forward_queue.append(initial_node)
        self.backward_queue.append(self.goal_node)

    def find_goal_state(self):
        fourth_side_cells_color = self.initial_node.sides_list[3].cells[3]
        fifth_side_cells_color = self.initial_node.sides_list[4].cells[3]
        sixth_side_cells_color = self.initial_node.sides_list[5].cells[1]
        first_side_cells_color = other_side_color(fifth_side_cells_color)
        second_side_cells_color = other_side_color(fourth_side_cells_color)
        third_side_cells_color = other_side_color(sixth_side_cells_color)
        first_side = Side([first_side_cells_color, first_side_cells_color, first_side_cells_color, first_side_cells_color])
        second_side = Side([second_side_cells_color, second_side_cells_color, second_side_cells_color, second_side_cells_color])
        third_side = Side([third_side_cells_color, third_side_cells_color, third_side_cells_color, third_side_cells_color])
        fourth_side = Side([fourth_side_cells_color, fourth_side_cells_color, fourth_side_cells_color, fourth_side_cells_color])
        fifth_side = Side([fifth_side_cells_color, fifth_side_cells_color, fifth_side_cells_color, fifth_side_cells_color])
        sixth_side = Side([sixth_side_cells_color, sixth_side_cells_color, sixth_side_cells_color, sixth_side_cells_color])
        return Rubik([first_side, second_side, third_side, fourth_side, fifth_side, sixth_side])

    def execute(self):
        while len(self.forward_queue) != 0 and len(self.backward_queue) != 0:
            if self.add_to_queue_check_other_queue(self.forward_queue, self.backward_queue):
                return True
            if self.add_to_queue_check_other_queue(self.backward_queue, self.forward_queue):
                return True

        return False

    def visited(self, rubik):
        if self.inside_queue(self.forward_queue, rubik):
            return True
        if self.inside_queue(self.backward_queue, rubik):
            return True

        return False

    def add_to_queue_check_other_queue(self, queue, other_queue):
        rubik = queue.pop(0)
        self.nodes_in_memory -= 1
        children = rubik.children_nodes()
        self.expanded_nodes += 1
        self.generated_nodes += len(children)
        self.depth_of_answer += 1
        for child_rubik in children:
            if not self.visited(child_rubik):
                queue.append(child_rubik)
                self.nodes_in_memory += 1
            else:
                if self.inside_queue(other_queue, child_rubik):
                    return True
