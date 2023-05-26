# Change Frame Range of all seleced Nodes:

import nuke

# Prompt the user to enter a new frame range
new_first_frame = nuke.getInput("Enter new first frame:")
new_last_frame = nuke.getInput("Enter new last frame:")

# Get the selected read nodes
read_nodes = nuke.selectedNodes("Read")

# Loop through each selected read node and set its frame range
for read_node in read_nodes:
    read_node["first"].setValue(int(new_first_frame))
    read_node["last"].setValue(int(new_last_frame))