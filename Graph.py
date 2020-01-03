from _collections import  defaultdict


class Graph:
    def __init__(self, initial_vertex):
        self.initial_vertex = initial_vertex
        self.graph = defaultdict(list)

    def add_children_nodes(self, rubik):
        children = rubik.children_nodes()
        self.graph[rubik].append(children)

