from Algorithm import Algorithm
from PriorityQueue import PriorityQueue


class UCS(Algorithm):

    def __init__(self, initial_vertex):
        super().__init__()
        self.inistial_vertex = initial_vertex
        self.frontier = PriorityQueue()
        self.frontier.insert(initial_vertex)
        self.explored = []

    def execute(self):
        while True:
            if self.frontier.is_empty():
                return False
            lowest_cost_rubik = self.frontier.delete()
            self.nodes_in_memory -= 1
            if self.goal_test(lowest_cost_rubik):
                return True
            self.nodes_in_memory += 1
            self.explored.append(lowest_cost_rubik)
            children = lowest_cost_rubik.children_nodes()
            self.depth_of_answer += 1
            # this is wrong completely wrong COMPLETELY
            self.generated_nodes += len(children)
            self.expanded_nodes += 1
            for child_rubik in children:
                child_rubik.path_cost = lowest_cost_rubik.path_cost + 1
                if not self.visited(child_rubik):
                    print(child_rubik.path_cost)
                    self.frontier.insert(child_rubik)
                    self.nodes_in_memory += 1
                elif self.inside_queue(self.frontier.queue, child_rubik):
                    for rubik_in_queue in self.frontier.queue:
                        if rubik_in_queue.equal(child_rubik):
                            if rubik_in_queue.path_cost > child_rubik.path_cost:
                                self.frontier.queue.remove(rubik_in_queue)
                                self.frontier.insert(child_rubik)

    def visited(self, rubik):
        if self.inside_queue(self.frontier.queue, rubik):
            return True
        if self.inside_queue(self.explored, rubik):
            return True

        return False
