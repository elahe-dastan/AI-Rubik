from Algorithm import Algorithm
from Graph import Graph


class IDS(Algorithm):

    def __init__(self, initial_rubik):
        super().__init__()
        self.graph = Graph(self.initial_rubik)
        self.initial_rubik = initial_rubik

    def execute(self, src, max_depth):
        for i in range(max_depth):
            if self.execute_DLS(src, i):
                self.depth_of_answer = i
                return True
        return False

    def execute_DLS(self, src, max_depth):
        if self.goal_test(src) : return True

        if max_depth <= 0 : return False

        self.graph.add_children_nodes(src)
        self.generated_nodes += len(src.children_nodes())
        self.nodes_in_memory += len(src.children_nodes())
        self.expanded_nodes += 1
        # for test
        for children in self.graph.graph[src]:
            for i in children:
                if self.execute_DLS(i, max_depth - 1):
                    return True
        return False


