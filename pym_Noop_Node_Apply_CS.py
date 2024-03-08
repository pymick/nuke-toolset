set cut_paste_input [stack 0]
version 13.1 v4
push $cut_paste_input
NoOp {
 name Apply_CS
 tile_color 0xff
 selected true
 xpos -680
 ypos 2091
 addUserKnob {20 Colorspace l "Apply Colorspace"}
 addUserKnob {22 python_button l "Apply Input Transform to selected nodes" T "import re\n\ndef get_read_colorspace():\n    # Get the input node connected to this NoOp node\n    input_node = nuke.toNode('\{\}.input'.format(nuke.thisNode().name()))\n    if input_node and input_node.Class() == 'Read':\n        # Get the 'colorspace' knob value from the connected Read node\n        colorspace_value = input_node\['colorspace'].getValue()\n        colorspace_str = input_node\['colorspace'].enumName(int(colorspace_value))\n\n        # Split the string only if it starts with specified keywords\n        keywords = \[\"ACES\", \"Input\", \"Output\", \"Utility\"]\n        for keyword in keywords:\n            if colorspace_str.startswith(keyword):\n                print('Read CS is:', colorspace_str)\n                colorspace_str_clean = colorspace_str.split(\"\\t\")\[0]\n                print('Clean is:', colorspace_str_clean)\n                return colorspace_str_clean  # Return cleaned string\n        else:\n            # If none of the keywords match, return the original string\n            colorspace_str_non_keyword = colorspace_str.split(\"\\t\")\[0]\n            colorspace_str_non_spaces = re.sub(r'\\s+', '', colorspace_str_non_keyword)\n            print('Non keyword CS is: ', colorspace_str_non_keyword)\n            return colorspace_str_non_spaces\n\n    else:\n        return None\n\nif __name__ == '__main__':\n    colorspace = get_read_colorspace()\n    if colorspace:\n        # Apply the colorspace to all selected Read nodes\n        for node in nuke.selectedNodes('Read'):\n            node\['colorspace'].setValue(colorspace)\n    else:\n        print(\"No connected Read node found.\")" +STARTLINE}
}
