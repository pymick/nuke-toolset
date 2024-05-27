set cut_paste_input [stack 0]
version 13.1 v4
push $cut_paste_input
Group {
 name WorldSpaceConverter
 selected true
 xpos 3640
 ypos 440
 addUserKnob {20 WorldSpaceConverter}
 addUserKnob {41 pulldown l "Render Engine Selection" T Output_Switch.pulldown}
 addUserKnob {26 ""}
 addUserKnob {20 manual_invert_controls l "Manual xyz invert" t "Use these checkboxes if something seems off and/or the render engine is unkown. " n 1}
 manual_invert_controls 0
 addUserKnob {41 invert_x l "Invert - x" T Output_Switch.invert_x}
 addUserKnob {41 invert_y l "Invert - y" T Output_Switch.invert_y}
 addUserKnob {41 invert_z l "Invert - z" T Output_Switch.invert_z}
 addUserKnob {20 endGroup n -1}
 addUserKnob {26 ""}
 addUserKnob {20 manual_shuffle_controls l "Manual xyz shuffle" t "Use this shuffle if something seems off and/or the render engine is unkown.\n\nred = x\ngreen = y\nblue = z   " n 1}
 manual_shuffle_controls 0
 addUserKnob {41 shuffle l "" -STARTLINE T Output_Switch.shuffle}
 addUserKnob {20 endGroup_1 l endGroup n -1}
}
 BackdropNode {
  inputs 0
  name BackdropNode1
  tile_color 0x595959ff
  label Redshift
  note_font_size 30
  xpos -308
  ypos -182
  bdwidth 136
  bdheight 64
 }
 BackdropNode {
  inputs 0
  name BackdropNode2
  tile_color 0x595959ff
  label Arnold
  note_font_size 30
  xpos -613
  ypos -183
  bdwidth 107
  bdheight 65
 }
 BackdropNode {
  inputs 0
  name BackdropNode3
  tile_color 0x595959ff
  label Cycles
  note_font_size 30
  xpos -933
  ypos -184
  bdwidth 107
  bdheight 67
 }
 BackdropNode {
  inputs 0
  name BackdropNode4
  tile_color 0x595959ff
  label Octane
  note_font_size 30
  xpos -1252
  ypos -184
  bdwidth 107
  bdheight 67
 }
 BackdropNode {
  inputs 0
  name BackdropNode5
  tile_color 0x595959ff
  label Vray
  note_font_size 30
  xpos -1558
  ypos -184
  bdwidth 77
  bdheight 68
 }
 Input {
  inputs 0
  name Input1
  xpos 40
  ypos -340
 }
 Dot {
  name Dot1
  xpos 74
  ypos -96
 }
set Nb00dbc00 [stack 0]
 Dot {
  name Dot2
  xpos -246
  ypos -96
 }
set Nb00db800 [stack 0]
 Dot {
  name Dot3
  xpos -566
  ypos -95
 }
set Nb00db400 [stack 0]
 Dot {
  name Dot4
  xpos -887
  ypos -95
 }
set Nb00db000 [stack 0]
 Dot {
  name Dot8
  xpos -1206
  ypos -95
 }
set Nb00dac00 [stack 0]
 Dot {
  name Dot10
  xpos -1527
  ypos -96
 }
 Dot {
  name Dot11
  xpos -1526
  ypos 84
 }
push $Nb00dac00
 Dot {
  name Dot9
  xpos -1206
  ypos 84
 }
push $Nb00db000
 Shuffle2 {
  fromInput1 {{0} B}
  fromInput2 {{0} B}
  mappings "4 black -1 -1 rgba.alpha 0 3 rgba.red 0 0 rgba.red 0 0 rgba.blue 0 2 rgba.green 0 1 rgba.green 0 1 rgba.blue 0 2"
  name Shuffle15
  xpos -921
  ypos -40
 }
 Expression {
  expr2 b*-1
  name Expression3
  xpos -921
  ypos -8
 }
 Dot {
  name Dot7
  xpos -887
  ypos 84
 }
push $Nb00db400
 Dot {
  name Dot6
  xpos -567
  ypos 84
 }
push $Nb00db800
 Expression {
  expr2 b*-1
  name Expression1
  xpos -280
  ypos -40
 }
 Dot {
  name Dot5
  xpos -246
  ypos 84
 }
push $Nb00dbc00
 Switch {
  inputs 6
  which {{pulldown}}
  name Output_Switch
  selected true
  xpos 40
  ypos 110
  addUserKnob {20 User}
  addUserKnob {4 pulldown l "Render engine selection" M {Unkown Redshift Arnold Cycles Octane Vray "" "" "" "" ""}}
  addUserKnob {26 ""}
  addUserKnob {20 manual_invert_controls l "Manual xyz invert" t "Use these checkboxes if something seems off and/or the render engine is unkown. " n 1}
  manual_invert_controls 0
  addUserKnob {6 invert_x l "Invert - x" +STARTLINE}
  addUserKnob {6 invert_y l "Invert - y" +STARTLINE}
  addUserKnob {6 invert_z l "Invert - z" +STARTLINE}
  addUserKnob {20 endGroup n -1}
  addUserKnob {26 ""}
  addUserKnob {20 manual_shuffle_controls l "Manual xyz shuffle" t "Use this shuffle if something seems off and/or the render engine is unkown.\n\nred = x\ngreen = y\nblue = z   " n 1}
  manual_shuffle_controls 0
  addUserKnob {41 shuffle l "" +STARTLINE T Shuffle1.shuffle}
  addUserKnob {20 endGroup_1 l endGroup n -1}
 }
 Expression {
  expr0 r*-1
  mix {{Output_Switch.invert_x}}
  name X_INVERT
  xpos 40
  ypos 170
 }
 Expression {
  expr1 g*-1
  mix {{Output_Switch.invert_y}}
  name Y_INVERT
  xpos 40
  ypos 230
 }
 Expression {
  expr2 b*-1
  mix {{Output_Switch.invert_z}}
  name Z_INVERT
  xpos 41
  ypos 290
 }
 Shuffle2 {
  fromInput1 {{0} B}
  in1 rgb
  out1 rgb
  fromInput2 {{0} B}
  mappings "3 rgba.red 0 0 rgba.red 0 0 rgba.green 0 1 rgba.green 0 1 rgba.blue 0 2 rgba.blue 0 2"
  name Shuffle1
  xpos 41
  ypos 350
 }
 Output {
  name Output1
  xpos 41
  ypos 590
 }
end_group
