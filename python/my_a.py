import adapy

def create_truss():
    # Define nodes
    nodes = {
        1: (0, 0),
        2: (1, 0),
        3: (2, 0),
        4: (0.5, 1),
        5: (1.5, 1),
        6: (1, 2)
    }

    # Define elements (members)
    elements = {
        1: (1, 4),
        2: (2, 4),
        3: (2, 5),
        4: (3, 5),
        5: (4, 6),
        6: (5, 6)
    }

    # Define supports
    supports = {1: (True, True), 3: (True, True)}

    # Define material properties and cross-sectional areas
    material = {'E': 200e9, 'A': 0.01}  # Young's modulus and cross-sectional area
    cross_section = {1: material, 2: material, 3: material, 4: material, 5: material, 6: material}

    # Create the truss model
    truss = adapy.Truss(nodes, elements, supports, cross_section)
    
    return truss

# Create the truss
truss = create_truss()
