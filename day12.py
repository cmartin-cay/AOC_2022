import networkx as nx
import numpy as np

with open("day12.txt") as f:
    grid = f.read().splitlines()
    grid = [list(word) for word in grid]

np_grid: np.array = np.array(grid)
end_pos = np.argwhere(np_grid == "E")
print(f"End pos {tuple(end_pos[0])}")

start_pos = np.where(np_grid == "S")
print(start_pos)
start_pos = (start_pos[0], start_pos[1])
all_a = np.where(np_grid == "a")
all_a = tuple(zip(*all_a))
print(len(all_a))

np_grid = np.char.replace(np_grid, "S", "a")
np_grid = np.char.replace(np_grid, "E", "z")
# print(np_grid)

G: nx.DiGraph = nx.grid_2d_graph(*np_grid.shape, create_using=nx.DiGraph)
G.remove_edges_from([(a, b) for a, b in G.edges if ord(np_grid[a]) - ord(np_grid[b]) <= -2])
print(G.out_edges((2, 5)))
print(len(nx.shortest_path(G, (20, 0), (20, 58))) - 1)

a_paths = []
for elem in all_a:
    try:
        a_paths.append(len(nx.shortest_path(G, elem, (20, 58))) - 1)
    except:
        pass
print(nx.multi_source_dijkstra(G, all_a, target=(20,58)))

print(min(a_paths))
