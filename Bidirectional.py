from Algorithm import Algorithm
from Graph import Graph
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
    # It's better to have a set not a list
    visited = []

    def __init__(self, initial_node):
        super().__init__(Graph(initial_node))
        self.initial_node = initial_node
        self.goal_node = self.find_goal_state()
        self.forward_queue.append(initial_node)
        self.visited.append(initial_node)
        self.backward_queue.append(self.goal_node)
        self.visited.append(self.goal_node)

    def find_goal_state(self):
        # first_side = Side([1, 1, 1, 1])
        # second_side = Side([2, 2, 2, 2])
        # third_side = Side([3, 3, 3, 3])
        # fourth_side = Side([4, 4, 4, 4])
        # fifth_side = Side([6, 6, 6, 6])
        # sixth_side = Side([5, 5, 5, 5])
        #
        # rubik = Rubik([first_side, second_side, third_side, fourth_side, fifth_side, sixth_side])
        # return rubik

        # There are so many goal states that we can not reach to all
        # of them so if we start from a goal that is unreachable code
        # doesn't finish
        sides_colors = [-1, -1, -1, -1, -1, -1]
        sides_colors[3] = self.initial_node.sides_list[3].cells[3]
        sides_colors[4] = self.initial_node.sides_list[4].cells[3]
        sides_colors[5] = self.initial_node.sides_list[5].cells[1]

        sides_colors[0] = other_side_color(sides_colors[4])
        sides_colors[1] = other_side_color(sides_colors[3])
        sides_colors[2] = other_side_color(sides_colors[5])

        sides_list = []
        for i in range(6):
            cells_list = []
            for j in range(4):
                cells_list.append(sides_colors[i])
            sides_list.append(Side(cells_list))

        return Rubik(sides_list)

    def execute(self):
        while len(self.forward_queue) != 0 and len(self.backward_queue) != 0:
            if self.add_to_queue_check_other_queue(self.forward_queue, self.backward_queue):
                return True
            if self.add_to_queue_check_other_queue(self.backward_queue, self.forward_queue):
                return True

        return False

    def is_visited(self, rubik):
        if self.inside_queue(self.visited, rubik):
            return True
        return False

    def add_to_queue_check_other_queue(self, queue, other_queue):
        rubik = queue.pop(0)
        self.nodes_in_memory -= 1
        # It doesn't answer correctly when the initial node and the
        # target node are the same
        children = rubik.children_nodes()
        self.update_number_of_nodes_info_after_expanding(len(children))
        for child_rubik in children:
            if not self.is_visited(child_rubik):
                self.visited.append(child_rubik)
                queue.append(child_rubik)
            else:
                self.nodes_in_memory -= 1
                if self.inside_queue(other_queue, child_rubik):
                    return True

