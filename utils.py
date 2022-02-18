import random
import math


def create_map(map_width=10, map_height=10, number_of_targets=5, number_of_obstacles=5):
    the_map = []
    i = 0
    j = 0
    target_points = []
    obstacle_points = {}
    starting_point = (random.randint(1, map_width-2), random.randint(1, map_height-2))

    while i < number_of_targets:
        temp_point = (random.randint(1, map_width-2), random.randint(1, map_height-2))
        if temp_point != starting_point:
            target_points.append(temp_point)
            i += 1

    while j < number_of_obstacles:
        temp_point = (random.randint(1, map_width-2), random.randint(1, map_height-2))
        if temp_point != starting_point and temp_point not in target_points:
            obstacle_points[temp_point] = random.choice([2, 3, 4])
            j += 1

    for h in range(map_height):
        row = []
        for w in range(map_width):
            if h == 0 or h == map_height-1:
                row.append('#')
            elif w == 0 or w == map_width-1:
                row.append('#')
            elif (w, h) == starting_point:
                row.append('s')
            elif (w, h) in target_points:
                row.append('t')
            elif (w, h) in obstacle_points.keys():
                row.append(str(obstacle_points[(w, h)]))
            else:
                row.append(' ')
        the_map.append(row)

    return the_map, starting_point, list(set(target_points)), obstacle_points


def create_graph(vertices, obstacle_points):
    the_graph = []

    for i in vertices:
        row = []
        for j in vertices:
            row.append(distance(i, j))
        the_graph.append(row)
    
    for obstacle, h in obstacle_points.items():
        for i, p in enumerate(vertices):
            for j, q in enumerate(vertices):
                if is_on_edge(p, q, obstacle):
                    the_graph[i][j] += h * 2
            
    return the_graph


def is_on_edge(start, end, point):
    start_x, start_y = start[0], start[1]
    end_x, end_y = end[0], end[1]
    point_x, point_y = point[0], point[1]

    if start_x != end_x:
        slope = (end_y - start_y) / (end_x - start_x)
        point_on = (point_y - start_y) == slope * (point_x - start_x)
        point_between = (min(start_x, end_x) <= point_x <= max(start_x, end_x)) and (min(start_y, end_y) <= point_y <= max(start_y, end_y))
        point_on_and_between = point_on and point_between
    else:
        point_on_and_between = (point_x == end_x) and (start_y <= point_y <= end_y)
    
    return point_on_and_between  


def distance(start, end):
    start_x, start_y = start[0], start[1]
    end_x, end_y = end[0], end[1]
    return round(math.sqrt(((start_x - end_x) ** 2) + ((start_y - end_y) ** 2)), 2)


def graph_cost(the_graph):
    cost = 0
    for row in the_graph:
        for weight in row:
            cost += weight
    return cost / 2


def min_in_graph(the_graph, number_of_vertices):
    minimum = 99999
    x, y = -1, -1
    for i in range(number_of_vertices):
        for j in range(number_of_vertices):
            if the_graph[i][j] > 0 and the_graph[i][j] < minimum:
                minimum = the_graph[i][j]
                x, y = i, j
    return x, y, minimum


def make_a_cycle(the_graph, the_mst, number_of_vertices):
    sub_graph = [[0 for column in range(number_of_vertices)] for row in range(number_of_vertices)]
    for i in range(number_of_vertices):
        for j in range(number_of_vertices):
            sub_graph[i][j] = the_graph[i][j] - the_mst[i][j]
    x, y, next_min = min_in_graph(sub_graph, number_of_vertices)
    the_mst[x][y] = the_mst[y][x] = next_min
    return the_mst
