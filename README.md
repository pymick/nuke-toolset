# PyMick Nuke Toolset

A collection of small Python scripts and node snippets that speed up everyday compositing work in [Foundry Nuke](https://www.foundry.com/products/nuke): managing Read nodes, tidying the node graph, fixing file paths and colorspaces, and handling 3D data.

## Usage

The tools come in two flavours:

| Type | How to use |
| --- | --- |
| **Python script** (`.py` containing Python) | Open the **Script Editor** (`Windows > Script Editor`), paste the code and run it. You can also add it to a menu or shelf via your `menu.py`. |
| **Node snippet** (`.py` containing Nuke node code, marked *Copy Paste to Nuke*) | Open the file in a text editor, copy everything, and paste it straight into the **Node Graph** with `Ctrl+V`. |

Most tools act on the **currently selected nodes**, so select what you want to change before running them.

### Adding a tool to a menu

```python
# menu.py
import nuke

toolset = "C:/path/to/nuke-toolset"
menu = nuke.menu("Nuke").addMenu("PyMick")
menu.addCommand("Snap to 80/30 Grid", "exec(open('%s/pym_snap_to_80_30_grid.py').read())" % toolset, "alt+s")
menu.addCommand("Move Nodes Down", "exec(open('%s/pym_move_selected_nodes.py').read())" % toolset)
```

---

## Tools at a glance

| Tool | Type | Works on | What it does |
| --- | --- | --- | --- |
| [Frame Range](#pym_frame-range) | Script | Selected Reads | Sets one frame range on several Read nodes |
| [Localization](#pym_localization) | Script | All Reads | Turns localization on for every Read |
| [Search and Replace](#pym_search-and-replace) | Script | All Reads | Moves file paths to a different drive letter |
| [List Read Drives](#pym_list-read-drives) | Script | All Read / Write / ReadGeo | Lists which drives the script pulls files from |
| [Read Grid Pattern](#pym_read-grid-pattern) | Script | Selected Reads | Lays out Read nodes in a tidy grid |
| [Snap to 80/30 Grid](#pym_snap_to_80_30_grid) | Script | Selected nodes | Snaps nodes onto a clean 80 × 30 grid |
| [Move Selected Nodes](#pym_move_selected_nodes) | Script | Selected nodes | Moves nodes 1000 units down |
| [Apply CS](#pym_noop_node_apply_cs) | Node snippet | Selected Reads | Copies the input colorspace from one Read to others |
| [WorldSpaceConverter](#pym_worldspaceconverter) | Node snippet | Position pass | Converts render-engine world position to Nuke world space |
| [Bake Camera with Axes](#pym_bake_camera_with_axes) | Script | Selected camera | Bakes a camera's world transform into a clean camera |
| [Wrap it Up](#pym_wrap_it_up) | Script (3rd party) | Whole script | Collects a script and all its media into one folder |

---

## Read node tools

### pym_Frame Range
**File:** `pym_Frame Range.py`

Gives every selected Read node the same frame range.

1. Select the Read nodes.
2. Run the script.
3. Enter the new **first** frame, then the new **last** frame.

Both values must be whole numbers.

### pym_Localization
**File:** `pym_Localization.py`

Sets the **localization policy** of *every* Read node in the script to `on`, so Nuke caches the media locally. This helps with slow network storage. No selection needed.

### pym_Search and Replace
**File:** `pym_Search and Replace.py`

Moves file paths from one drive to another, e.g. after media was copied from `Y:` to `T:`.

1. Run the script. A **Select Drive** dialog opens.
2. In **Current Path**, enter the path (or part of a path) to replace, e.g. `Y:/projects/show_a`.
3. In **Select a drive**, pick the new drive letter (`C:`, `T:`, `Y:`, `Z:`).
4. Click **OK**.

The script replaces the path in the `file` and `proxy` knobs of **all Read nodes** in the script, keeping everything after the drive letter. In the example above, `Y:/projects/show_a` becomes `T:/projects/show_a`.

> **Note:** The search text is treated as a regular expression. Use forward slashes (`/`) in paths, and escape special characters such as `.` or `(` if a match fails. To offer other drives in the dropdown, edit the `self.options` tuple in the script.

### pym_List Read Drives
**File:** `pym_List Read Drives.py`

Opens a window listing every drive letter the script reads from or writes to, with the nodes that use it:

```
T:: Read1, Read4, Write2
Y:: Read2, ReadGeo1
```

It checks Read, Write and ReadGeo nodes. This is handy for spotting stray local (`C:`) paths before sending a script to the farm or to another artist.

### pym_Read Grid Pattern
**File:** `pym_Read Grid Pattern.py`

Lays out the selected Read nodes in a grid of **4 columns**, with 200 units between nodes. Nodes are ordered by their current position, and the grid starts at the top-left node of the selection.

---

## Node graph tools

### pym_snap_to_80_30_grid
**File:** `pym_snap_to_80_30_grid.py`

Snaps every selected node to the nearest point on an **80 (x) × 30 (y)** grid, which keeps the node graph neat and evenly aligned. Each node's position is offset to its centre before rounding, so standard-sized nodes line up exactly.

Bind it to a hotkey for quick tidying (see [Adding a tool to a menu](#adding-a-tool-to-a-menu)).

### pym_move_selected_nodes
**File:** `pym_move_selected_nodes.py`

Moves all selected nodes **1000 units down** in the node graph. This is a quick way to make room above a branch or move a block of nodes out of the way. To change the distance, edit the `1000` in the script.

---

## Colour tools

### pym_Noop_Node_Apply_CS
**File:** `pym_Noop_Node_Apply_CS.py` (*Copy Paste to Nuke*)

A red **NoOp** node called `Apply_CS` that copies the **input colorspace** of one Read node to many others.

1. Paste the snippet into the Node Graph.
2. Connect its input to the Read node that has the correct colorspace.
3. Select all the Read nodes that should get the same colorspace.
4. In the `Apply_CS` properties, open the **Apply Colorspace** tab and click **Apply Input Transform to selected nodes**.

It works with OCIO/ACES colorspace names (`ACES…`, `Input…`, `Output…`, `Utility…`) as well as Nuke's default colorspaces.

---

## 3D tools

### pym_WorldSpaceConverter
**File:** `pym_WorldSpaceConverter.py` (*Copy Paste to Nuke*)

A Group node that converts world-position passes (e.g. *P*, *World Position*) from different 3D render engines into **Nuke's native world space**. This lets you use them with Nuke tools such as PositionToPoints or position-based masks.

1. Paste the snippet into the Node Graph.
2. Connect the position pass to its input.
3. Choose the engine in **Render Engine Selection**:

| Engine | Conversion |
| --- | --- |
| Unknown | Passes the data through unchanged |
| Redshift | Inverts Z |
| Arnold | No change needed |
| Cycles (Blender) | Swaps Y/Z and inverts Z (Z-up → Y-up) |
| Octane | No change needed |
| V-Ray | No change needed |

If the result still looks wrong, or the engine is not listed, use the manual controls:

- **Manual xyz invert:** flips the X, Y or Z axis on its own.
- **Manual xyz shuffle:** reorders the channels (red = x, green = y, blue = z).

### pym_bake_camera_with_axes
**File:** `pym_bake_camera_with_axes.py`

Takes a camera whose position comes from parent **Axis** nodes (or any transform chain) and creates a new standalone **Camera2** with that world position baked into its own **translate** and **rotate** values.

1. Select the camera node.
2. Run the script.

This only bakes the current frame, so use it for **static cameras**. The script needs `numpy` in Nuke's Python environment.

---

## Pipeline tools

### pym_Wrap_it_Up
**File:** `pym_Wrap_it_Up.py`

**WrapItUp 2.1** by **Max van Leeuwen** ([maxvanleeuwen.com/WrapItUp](https://maxvanleeuwen.com/WrapItUp)). It is included here for convenience; all credit goes to the original author.

It collects a Nuke script together with all its media, fonts and gizmos, and copies everything into one folder, along with a relinked copy of the `.nk` file. Use it for archiving, handing a shot over, or sending work to a client or another studio.

- Run it inside Nuke to open the WrapItUp window, where you can preview the file list and pick options.
- It can also run from the terminal without the UI. Main flags: `-nk <script>` and `-o <output folder>` (both required), and `-s` to start copying (without it you only get a preview). See the usage text in the script for all flags.

---

## Requirements

- Foundry Nuke 13+ (the snippets were saved with Nuke 13.1; newer versions should also work)
- PySide2 (ships with Nuke) for the tools that open a window
- `numpy` for *Bake Camera with Axes*

## Author

**Maximilian Schlick** ([pymick](https://github.com/pymick)), except *Wrap it Up* by Max van Leeuwen.
