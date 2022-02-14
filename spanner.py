from map_creator import create_map

the_map, starting_point, target_points = create_map()

print("targets: ", target_points)
print("start: ", starting_point)
for row in the_map:
    print(row)

