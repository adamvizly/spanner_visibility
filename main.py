from utils import create_map, create_graph, graph_cost, make_a_cycle
from spanner import primsAlgorithm


the_map, starting_point, target_points, obstacle_points = create_map()

print("targets: ", target_points)
print("start: ", starting_point)
print("obstacles: ", obstacle_points)
print("the map: ")
for row in the_map:
    print(row)

vertices = target_points
vertices.append(starting_point)
the_graph = create_graph(vertices, obstacle_points)
print("vertices: ", vertices)
print("the graph: ")
for row in the_graph:
    print(row)

the_mst = primsAlgorithm(the_graph, len(vertices))
print("the MST: ")
for row in the_mst:
    print(row)

the_mst_cost = graph_cost(the_mst)

the_cycle = make_a_cycle(the_graph, the_mst, len(vertices))
print("the MST with a cycle: ")
for row in the_cycle:
    print(row)

the_cycle_cost = graph_cost(the_cycle)

print("MST cost: ", the_mst_cost)
print("MST with cycle cost: ", the_cycle_cost)
