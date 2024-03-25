import numpy as np
from stl import mesh

# Extracting information from the image
# Assuming a 2D truss with members of same length
# Member length = 1 unit
# Nodes: A, B, C, D, E, F, G, H
# Members: AB, BC, CD, DE, EF, FG, GH, AH

# Defining node coordinates
nodes = np.array([
    [0, 0, 0],  # A
    [1, 0, 0],  # B
    [1, 1, 0],  # C
    [0.5, 2, 0],  # D
    [0, 2, 0],  # E
    [-0.5, 2, 0],  # F
    [-1, 1, 0],  # G
    [-1, 0, 0],  # H
])

# Defining faces (triangles) for each member
faces = []

# Member AB
faces.append([nodes[0], nodes[1], nodes[7]])

# Member BC
faces.append([nodes[1], nodes[2], nodes[7]])

# Member CD
faces.append([nodes[2], nodes[3], nodes[7]])

# Member DE
faces.append([nodes[3], nodes[4], nodes[7]])

# Member EF
faces.append([nodes[4], nodes[5], nodes[7]])

# Member FG
faces.append([nodes[5], nodes[6], nodes[7]])

# Member GH
faces.append([nodes[6], nodes[7], nodes[0]])

# Member AH
faces.append([nodes[0], nodes[7], nodes[3]])

# Create and save the STL mesh
my_mesh = mesh.Mesh(np.array(faces))
my_mesh.save("truss_design.stl")
