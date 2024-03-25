import trusspy
import matplotlib.pyplot as plt

# Define the problem
problem = trusspy.Problem()

# Define the truss structure
# Add nodes
node1 = problem.add_node(0, 0)
node2 = problem.add_node(5, 0)
node3 = problem.add_node(2.5, 3)

# Add elements
element1 = problem.add_element(node1, node3, area=1, material="steel")
element2 = problem.add_element(node2, node3, area=1, material="steel")

# Define material properties
problem.add_material("steel", density=7850, young_modulus=2.1e11)  # Example values

# Define loads
problem.add_point_load(node3, load_y=-1000)  # Example load

# Run optimization
solution = problem.optimize()

# Get optimized design
optimized_structure = solution.get_structure()

# Plot the optimized truss
fig, ax = plt.subplots()
for element in optimized_structure.elements:
    node1 = element.node1
    node2 = element.node2
    ax.plot([node1.x, node2.x], [node1.y, node2.y], 'k-')

# Plot nodes
for node in optimized_structure.nodes:
    ax.plot(node.x, node.y, 'ro')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Optimized Truss Structure')
plt.grid(True)
plt.axis('equal')
plt.show()
