import math
import sys

def decompose_matrix(matrix):
    # Extract translation
    translate = (matrix[0][3], matrix[1][3], matrix[2][3])
    
    # Extract rotation
    rotation = matrix[:3, :3]
    sx = math.sqrt(rotation[0][0] * rotation[0][0] + rotation[1][0] * rotation[1][0])
    singular = sx < 1e-6
    if not singular:
        rx = math.atan2(rotation[2][1], rotation[2][2])
        ry = math.atan2(-rotation[2][0], sx)
        rz = math.atan2(rotation[1][0], rotation[0][0])
    else:
        rx = math.atan2(-rotation[1][2], rotation[1][1])
        ry = math.atan2(-rotation[2][0], sx)
        rz = 0
    
    # Convert radians to degrees
    rx = math.degrees(rx)
    ry = math.degrees(ry)
    rz = math.degrees(rz)
    
    return translate, (rx, ry, rz)

def bake_camera_transform(camera_node):
    world_matrix = np.array(camera_node['world_matrix'].getValue())
    
    # Reshape the matrix into a 4x4 matrix
    world_matrix = np.reshape(world_matrix, (4, 4))
    
    # Decompose the world matrix into translate and rotation
    translate, rotate = decompose_matrix(world_matrix)
    
    # Create a new camera node
    new_camera = nuke.createNode("Camera2")
    
    # Apply translation and rotation to the new camera
    new_camera['translate'].setValue(translate)
    new_camera['rotate'].setValue(rotate)

# Specify the camera node to bake
camera_node = nuke.selectedNode()

# Call the function to bake transform
bake_camera_transform(camera_node)
