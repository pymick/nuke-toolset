import nuke

# Get the selected Read nodes
selected_nodes = nuke.selectedNodes("Read")

# Sort the nodes by their x and y positions
sorted_nodes = sorted(selected_nodes, key=lambda node: (node.xpos(), node.ypos()))

# Calculate the grid spacing
x_spacing = 200
y_spacing = 200

# Set the initial grid position
grid_x = sorted_nodes[0].xpos()
grid_y = sorted_nodes[0].ypos()

# Loop through the sorted nodes and set their positions
for i, node in enumerate(sorted_nodes):
    node.setXpos(grid_x)
    node.setYpos(grid_y)

    # Update the grid position
    grid_x += x_spacing
    if (i + 1) % 4 == 0:
        grid_x = sorted_nodes[0].xpos()
        grid_y += y_spacing