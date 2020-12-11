
biome_map = []
with open("input_3.txt", "rt") as forest_file:
    for line in forest_file.readlines():
        row = line.split()
        biome_map.append(row)

print(biome_map)
