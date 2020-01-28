def side_completed(side):
    for j in range(len(side.cells) - 1):
        if side.cells[j] != side.cells[j + 1]:
            return False
    return True


class Algorithm:

    def __init__(self, graph):
        self.inital_graph = graph
        self.graph = graph
        self.generated_nodes = 0
        self.expanded_nodes = 0
        self.depth_of_answer = 0
        self.nodes_in_memory = 0

    def goal_test(self, rubik):
        for i in range(len(rubik.sides_list)):
            side = rubik.sides_list[i]
            if not side_completed(side):
                return False
        return True

    def inside_queue(self, queue, rubik):
        for rubik_in_queue in queue:
            if rubik_in_queue.equal(rubik):
                return True
        return False

    def update_number_of_nodes_info_after_expanding(self, number_of_children):
        self.generated_nodes += number_of_children
        self.nodes_in_memory += number_of_children
        self.expanded_nodes += 1

    def reset_number_of_nodes_info(self):
        self.generated_nodes = 0
        self.nodes_in_memory = 0
        self.expanded_nodes = 0

    def remove_graph(self):
        self.graph = self.inital_graph
