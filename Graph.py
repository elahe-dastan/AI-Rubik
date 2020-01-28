class Graph:
    def __init__(self, initial_vertex):
        self.initial_vertex = initial_vertex
        self.graph = {}

    def add_children_nodes(self, rubik):
        children = rubik.children_nodes()
        self.graph[rubik] = children

    # # a little silly
    # def number_of_children(self, src):
    #     return len(src.children_nodes())
