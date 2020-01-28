from Algorithm import Algorithm
from Graph import Graph
from PriorityQueue import PriorityQueue


class UCS(Algorithm):

    def __init__(self, initial_vertex):
        super().__init__(Graph(initial_vertex))
        self.inistial_vertex = initial_vertex
        self.frontier = PriorityQueue()
        self.frontier.insert(initial_vertex)
        self.explored = []

    def execute(self):
        while True:
            if self.frontier.is_empty():
                return False
            lowest_cost_rubik = self.frontier.delete()
            if self.goal_test(lowest_cost_rubik):
                return True
            self.explored.append(lowest_cost_rubik)
            children = lowest_cost_rubik.children_nodes()
            self.update_number_of_nodes_info_after_expanding(len(children))
            for child_rubik in children:
                child_rubik.path_cost = lowest_cost_rubik.path_cost + 1
                if not self.visited(child_rubik):
                    print(child_rubik.path_cost)
                    self.frontier.insert(child_rubik)
                else:
                    self.nodes_in_memory -= 1
                    for rubik_in_queue in self.frontier.queue:
                        if rubik_in_queue.equal(child_rubik):
                            if rubik_in_queue.path_cost > child_rubik.path_cost:
                                self.frontier.queue.remove(rubik_in_queue)
                                self.frontier.insert(child_rubik)
                            else:
                                break

    def visited(self, rubik):
        if self.inside_queue(self.frontier.queue, rubik):
            return True
        if self.inside_queue(self.explored, rubik):
            return True
        return False
