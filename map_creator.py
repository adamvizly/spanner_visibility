import random


def create_map(map_width=10, map_height=10, number_of_targets=5):
    the_map = []
    i = 0
    target_points = []
    starting_point = (random.randint(1, map_width-2), random.randint(1, map_height-2))

    while i < number_of_targets:
        temp_point = (random.randint(1, map_width-2), random.randint(1, map_height-2))
        if temp_point != starting_point:
            target_points.append(temp_point)
            i += 1

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
            elif w == random.randint(1, map_width-2):
                row.append(random.choice(['2', '3', '4']))
            else:
                row.append(' ')
        the_map.append(row)

    return the_map, starting_point, target_points
