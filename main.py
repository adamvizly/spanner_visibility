from map_creator import create_map, create_graph
from spanner import primsAlgorithm


the_map, starting_point, target_points, obstacle_points = create_map(6,5,3,4)

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
