import nuke_internal as nuke
import re
import nukescripts
import os

def __NodeHasKnobWithName(node, name):
  try:
    node[name]
  except NameError:
    return False
  else:
    return True

def __NodeHasFileKnob(node):
  return __NodeHasKnobWithName(node, 'file')

def __NodeHasProxyKnob(node):
  return __NodeHasKnobWithName(node, 'proxy')

def __ReplaceKnobValue(searchstr, replacestr, knob):
  v = knob.value()
  if v:
    repl = re.sub(searchstr, replacestr, v)
    knob.setValue(repl)

def search_replace(searchstr, replacestr):
  """ Search/Replace in Reads and Writes. """
  fileKnobNodes = [i for i in nuke.selectedNodes() if __NodeHasFileKnob(i)]
  proxyKnobNodes = [i for i in nuke.selectedNodes() if __NodeHasProxyKnob(i)]
  if not fileKnobNodes and not proxyKnobNodes: raise ValueError("No nodes selected")

  for i in fileKnobNodes: __ReplaceKnobValue(searchstr, replacestr, i['file'])
  for i in proxyKnobNodes: __ReplaceKnobValue(searchstr, replacestr, i['proxy'])

class DriveDialog(nukescripts.PythonPanel):
    def __init__(self, width=700):
        nukescripts.PythonPanel.__init__(self, "Select Drive")
        self.setMinimumSize(width, 1)

        # Create a string input field for the user to enter a path
        self.path_knob = nuke.String_Knob("current_path", "Current Path")
        self.addKnob(self.path_knob)

        # Define the options for the dropdown menu
        self.options = ("C:", "T:", "Y:", "Z:")

        # Create a dropdown menu for the user to select a drive
        self.drive_knob = nuke.Enumeration_Knob("selected_drive", "Select a drive", self.options)
        self.addKnob(self.drive_knob)

    def showModalDialog(self):
        result = nukescripts.PythonPanel.showModalDialog(self)

        # If the user clicked the "OK" button, save the selected option and the path input
        if result:
            selected_index = int(self.drive_knob.getValue())
            selected_drive = self.options[selected_index]
            current_path = self.path_knob.getValue()
            # Modify the current_path string to have the new drive letter
            path_components = os.path.splitdrive(current_path)
            updated_path = selected_drive + path_components[1]
            return updated_path, current_path  # return both updated_path and current_path as a tuple
        else:
            return None, None  # return None for both updated_path and current_path if user clicked "Cancel"

drive_dialog = DriveDialog(width=700)
updated_path, current_path = drive_dialog.showModalDialog()

read_nodes = []

for node in nuke.allNodes():
    if node.Class() == "Read":
        read_nodes.append(node)

nuke.selectAll()
for node in read_nodes:
    node.setSelected(True)

search_replace(current_path, updated_path)