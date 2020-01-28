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

ids_algorithm = IDS(Graph(initial_rubik))
ids_algorithm.execute()

bidirectional_algorithm = Bidirectional(initial_rubik)
bidirectional_algorithm.execute()

ucs_algorithm = UCS(initial_rubik)
ucs_algorithm.execute()