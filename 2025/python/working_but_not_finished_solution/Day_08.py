# Advent of Code 2025
# Szombathy Dominik
# 2025.12.12

# Day 8 - Playground

import Functions as F
import numpy as np
import matplotlib.pyplot as plt

File = F.OpenFile("/Volumes/THYMac/Users/dominikszombathy/Programming/DomcsisEpicTinkerBox/AdventOfCode/Advent_of_Code_2025/Junction_box_coordinates.txt")

def GetCoordinates(Line: str) -> list:
    Coordinate_str = Line.split(",")
    Coordinates = []
    for item in Coordinate_str:
        Coordinates.append(int(item))
    return Coordinates

Coordinates = []
for lines in range(1000):
    Coordinates.append(GetCoordinates(File[lines]))

def GetDistance(Coordinate_1, Coordinate_2):
    return np.sqrt((Coordinate_1[0] - Coordinate_2[0])**2 + (Coordinate_1[1] - Coordinate_2[1])**2 + (Coordinate_1[2] - Coordinate_2[2])**2 )

def DistanceMatrix(Coordinates: list):
    D = [[0 for _ in range(len(Coordinates))] for _ in range(len(Coordinates))]
    for i in range(len(Coordinates)):
        for j in range(i, len(Coordinates)):
            D[i][j] = GetDistance(Coordinates[i], Coordinates[j])
    return D


def distances(Coordinates: list):
    D = []
    I = []
    for i in range(len(Coordinates)):
        for j in range(i + 1, len(Coordinates)):
            D.append(GetDistance(Coordinates[i], Coordinates[j]))
            I.append([i, j])
    return D, I

Distance, Index = distances(Coordinates)

#import numpy as np
#import matplotlib.pyplot as plt
#
#N = len(Coordinates)  # number of junction boxes
#
#H = np.zeros((N, N))
#
#for d, (i, j) in zip(Distance, Index):
#    H[i, j] = d
#    H[j, i] = d  # symmetry

#plt.figure(figsize=(8, 6))
#plt.imshow(H)
#plt.colorbar(label="Distance")
#plt.xlabel("Index i")
#plt.ylabel("Index j")
#plt.title("Distance Heatmap")
#plt.tight_layout()
  

minInd = np.argsort(Distance)[:1000]

print(minInd, len(minInd), len(Distance))

def ConnectBoxes(Index: list, box_indices: list):
    Connections = [ [] for i in range(1000)]
    for i in Index:
        Connections[box_indices[i][0]].append(box_indices[i][1])

    return Connections

def merge_box_connections(Connections):
    MergedConnections = [[] for _ in range(1000)]

    for i in range(len(Connections)):
        MergedConnections[i] = sorted(set(
            [i] +
            Connections[i] +
            [k for j in Connections[i] for k in Connections[j]]
        ))

    return MergedConnections


Connected_boxes = merge_box_connections(ConnectBoxes(minInd, Index))
def box_robit_length(Connected_boxes):
    orbits = []
    for i in range(len(Connected_boxes)):
        orbits.append(len(Connected_boxes[i]))
    
    return orbits

print(sorted(box_robit_length(Connected_boxes)))


#########  2025.12.18
import numpy as np

def read_coordinates(path):
    coords = []
    with open(path) as f:
        for line in f:
            coords.append(list(map(int, line.strip().split(","))))
    return coords

Coordinates = read_coordinates(
    "/Volumes/THYMac/Users/dominikszombathy/Programming/DomcsisEpicTinkerBox/AdventOfCode/Advent_of_Code_2025/Junction_box_coordinates.txt"
)


def distances(coords):
    D = []
    I = []
    N = len(coords)

    for i in range(N):
        for j in range(i + 1, N):
            d = np.linalg.norm(np.array(coords[i]) - np.array(coords[j]))
            D.append(d)
            I.append((i, j))

    return np.array(D), I

Distance, Index = distances(Coordinates)

shortest = np.argsort(Distance)[:1000]

def build_graph(edge_indices, pairs, N):
    G = [[] for _ in range(N)]

    for idx in edge_indices:
        a, b = pairs[idx]
        G[a].append(b)
        G[b].append(a)   # IMPORTANT: undirected

    return G

Connections = build_graph(shortest, Index, len(Coordinates))

def connected_components(graph):
    visited = [False] * len(graph)
    components = []

    for start in range(len(graph)):
        if visited[start]:
            continue

        stack = [start]
        comp = set()

        while stack:
            v = stack.pop()
            if visited[v]:
                continue

            visited[v] = True
            comp.add(v)

            for n in graph[v]:
                if not visited[n]:
                    stack.append(n)

        components.append(comp)

    return components

components = connected_components(Connections)
print(components)
orbit_sizes = sorted(len(c) for c in components)

print("Orbit sizes:", orbit_sizes)
print(orbit_sizes[-1] * orbit_sizes[-2] * orbit_sizes[-3])


# part 2

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.components = n

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False

        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra

        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        self.components -= 1
        return True

Distance, Index = distances(Coordinates)
order = np.argsort(Distance)   

uf = UnionFind(len(Coordinates))

for idx in order:
    a, b = Index[idx]

    merged = uf.union(a, b)
    if merged and uf.components == 1:
        # THIS is the last edge needed
        x1 = Coordinates[a][0]
        x2 = Coordinates[b][0]
        answer = x1 * x2
        print("Answer:", answer)
        break



def find_component(components, x):
    for i, s in enumerate(components):
        if x in s:
            return i
    return None

for idx in order:
    a, b = Index[idx]

    ia = find_component(components, a)
    ib = find_component(components, b)

    if ia == ib:
        continue

    components[ia] |= components[ib]
    components.pop(ib)

    if len(components) == 1:
        print("Answer:", Coordinates[a][0] * Coordinates[b][0])
        break