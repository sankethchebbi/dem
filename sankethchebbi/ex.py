# from slientruss3d.truss import Truss, Member
# from slientruss3d.type  import SupportType, MemberType
# from slientruss3d.plot  import TrussPlotter

# import random

# # Define joints
# joints = [
#     [[0, 0, 0], "PIN"],
#     [[10, 0, 0], "PIN"],
#     [[20, 0, 0], "PIN"],
#     [[0, 10, 0], "PIN"],
#     [[10, 10, 0], "NO"],
#     [[20, 10, 0], "PIN"],
#     [[0, 20, 0], "PIN"],
#     [[10, 20, 0], "PIN"],
#     [[20, 20, 0], "PIN"]
# ]

# # Define members
# members = [
#     [[0, 1], [1, 2e7, 1]],
#     [[1, 2], [1, 2e7, 1]],
#     [[3, 4], [1, 2e7, 1]],
#     [[4, 5], [1, 2e7, 1]],
#     [[6, 7], [1, 2e7, 1]],
#     [[7, 8], [1, 2e7, 1]],
#     [[0, 3], [1, 2e7, 1]],
#     [[1, 4], [1, 2e7, 1]],
#     [[2, 5], [1, 2e7, 1]],
#     [[3, 6], [1, 2e7, 1]],
#     [[4, 7], [1, 2e7, 1]],
#     [[5, 8], [1, 2e7, 1]]
# ]

# # Example forces
# forces = [[4, [0, -1000, 0]]]

# # Create truss
# truss = Truss(3, joints=joints, members=members, forces=forces)


# # Member types for optimization
# types = [MemberType(i, random.uniform(1e7, 3e7), random.uniform(0.1, 1)) for i in range(1, 10)]

# # GA parameters
# max_iter = 100
# patience = 20

# # Create GA optimizer
# ga = GA(truss, types, 30000, 10, max_iter, patience)

# # Run optimization
# min_gene, fitness, final_pop, history = ga.Evolve()

# # Get optimized member types
# truss.SetMemberTypes(ga.TranslateGene(min_gene))

# # Print solution
# print(truss.Solve())


import matplotlib.pyplot as plt
from sankethchebbi.truss import Truss
from sankethchebbi.plot import TrussPlotter


def TestLoadFromJSON():
    # -------------------- Global variables --------------------
    # Files settings:
    TEST_FILE_NUMBER = 0
    TEST_LOAD_CASE   = 0
    TEST_INPUT_FILE  = f"./data/bar-{TEST_FILE_NUMBER}_input_{TEST_LOAD_CASE}.json"
    TEST_OUTPUT_FILE = f"./data/bar-{TEST_FILE_NUMBER}_output_{TEST_LOAD_CASE}.json"

    # Truss dimension setting:
    TRUSS_DIMENSION  = 3
    # ----------------------------------------------------------

    # Truss object:
    truss = Truss(dim=TRUSS_DIMENSION)

    # Read data in [.json]:
    truss.LoadFromJSON(TEST_INPUT_FILE)

    # Do direct stiffness method:
    truss.Solve()
    plotter = TrussPlotter(truss)
    plotter.Plot()
    plt.savefig("truss_plot.png")
    # Dump all the structural analysis results into a .json file:
    truss.DumpIntoJSON(TEST_OUTPUT_FILE)


print(TestLoadFromJSON())
