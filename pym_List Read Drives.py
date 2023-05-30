import os
import nuke
from PySide2 import QtWidgets

# Create an empty dictionary to store the drive names and their corresponding nodes
drive_dict = {}

# Loop through all the nodes in the script
for node in nuke.allNodes():
    # Check if the node is a Read, Write, or ReadGeo node
    if node.Class() in ["Read", "Write", "ReadGeo2"]:
        # Get the file path from the node's file knob
        file_path = node["file"].value()
        # Get the drive name from the file path
        drive_name = os.path.splitdrive(file_path)[0]
        # Add the node name to the dictionary with the drive name as the key
        if drive_name not in drive_dict:
            drive_dict[drive_name] = [node.name()]
        else:
            drive_dict[drive_name].append(node.name())

# Create a QListWidget to display the list of drives and their corresponding nodes
list_widget = QtWidgets.QListWidget()

# Loop through the dictionary and add each drive and its corresponding nodes to the QListWidget
for drive, nodes in drive_dict.items():
    list_widget.addItem(drive + ": " + ", ".join(nodes))

# Create a QDialog window to display the QListWidget
window = QtWidgets.QDialog()
window.setWindowTitle('List of Drives and Nodes')
window.setLayout(QtWidgets.QVBoxLayout())
window.layout().addWidget(list_widget)

# Show the window
window.exec_()