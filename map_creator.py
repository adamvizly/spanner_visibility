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
            for obstacle, h in obstacle_points.items():
                if is_on_edge(i, j, obstacle):
                    row.append(distance(i, j) + h)
                else:
                    row.append(distance(i, j))
        the_graph.append(row)
    
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