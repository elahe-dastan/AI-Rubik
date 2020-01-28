from Algorithm import Algorithm
from Graph import Graph


class IDS(Algorithm):

    def __init__(self, graph):
        super().__init__(graph)
        # self.graph = Graph(initial_rubik)
        # self.initial_rubik = initial_rubik

    # src is a rubik which is a node of graph
    def execute(self, initial_depth, max_depth):
        for depth in range(initial_depth, max_depth):
            self.reset_number_of_nodes_info()
            self.remove_graph()
            if self.execute_DLS(self.graph.initial_vertex, depth):
                self.depth_of_answer = depth
                return True
        return False

    def execute_DLS(self, src, max_depth):
        if self.goal_test(src) : return True

        if max_depth <= 0 : return False

        self.graph.add_children_nodes(src)
        self.update_number_of_nodes_info_after_expanding(len(src.children_nodes()))
        # for test
        for child in self.graph.graph[src]:
            if self.execute_DLS(child, max_depth - 1):
                return True
        return False

