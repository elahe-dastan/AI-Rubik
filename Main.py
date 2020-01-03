from Bidirectional import Bidirectional
from Graph import Graph
from IDS import IDS
from Rubik import Rubik
from Side import Side
from UCS import UCS

number_of_sides = 6

print("Enter the initial state")

sides_list = []
for i in range(number_of_sides):
    side = Side(list(map(int, input().split())))
    sides_list.append(side)

initial_rubik = Rubik(sides_list)
# graph = Graph(initial_rubik)
# graph.add_children_nodes(initial_rubik)
# ids_instance = IDS(initial_rubik)
# ids_instance.execute(initial_rubik, 10)
# bidirectional_instance = Bidirectional(initial_rubik)
# bidirectional_instance.execute()
UCS_instance = UCS(initial_rubik)
UCS_instance.execute()

# for k,v in graph.graph.items():
#     print("key")
#     print(k.print_rubik())
#     for i in range(len(v[0])):
#         print("value")
#         v[0][i].print_rubik()
# print(graph.graph)
# initial_rubik.right_rotation(3)
# initial_rubik.print_rubik()
# tmp = initial_rubik.children_nodes()
# for i in range(len(tmp)):
#     rubik = tmp[i]
#     rubik.print_rubik()
#     print()