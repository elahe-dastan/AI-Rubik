def side_completed(side):
    for j in range(len(side.cells) - 1):
        if side.cells[j] != side.cells[j + 1]:
            return False
    return True


class Algorithm:

    def __init__(self):
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
