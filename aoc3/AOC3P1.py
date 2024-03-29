def get_biome():
    biome_map = []
    with open("input_3.txt", "rt") as forest_file:
        for line in forest_file.readlines():
            biome_map.append(line.rstrip("\n"))
    return biome_map


def traverse(x_move, y_move, biome_map):
    end_col = len(biome_map) # Last col of biome
    pos_x = 0  # Start at top-left corner of biome
    pos_y = 0
    trees = 0

    for i in range(len(biome_map)):
        pos_x += x_move
        pos_y += y_move
        if pos_y > len(biome_map)-1:
            break  # Stop if reached below last row
        if pos_x >= len(biome_map[pos_y]):
            for j in range(pos_y, len(biome_map)):
                biome_map[j] += biome_map[j]  # Repeat row pattern

        curr_marker = biome_map[pos_y][pos_x]
        if curr_marker == '#':
            trees += 1  # Tree marked by #

    return trees


def count_trees(x_move, y_move):
    forest = get_biome()
    trees = traverse(x_move, y_move, forest)
    return trees


x_move = 1  # Coordinates to move by
y_move = 1
trees = count_trees(x_move, y_move)
print(trees)

x_move = 3  # Coordinates to move by
y_move = 1
trees = count_trees(x_move, y_move)
print(trees)

x_move = 5  # Coordinates to move by
y_move = 1
trees = count_trees(x_move, y_move)
print(trees)

x_move = 7  # Coordinates to move by
y_move = 1
trees = count_trees(x_move, y_move)
print(trees)

x_move = 1  # Coordinates to move by
y_move = 2
trees = count_trees(x_move, y_move)
print(trees)



