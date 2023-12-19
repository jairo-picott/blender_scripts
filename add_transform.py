import bpy
import math

location_x = -21.051
location_z = 12.75

rotation_z = 90

selected_objects = bpy.context.selected_objects

def update_location(obj, x, change_x, y, change_y, z, change_z):
    if change_x:
        obj.location.x = x
    if change_y:
        obj.location.y = y
    if change_z:
        obj.location.z = z

    print('New object {} Location: {}, {}, {}'.format(obj.name, x, y, z))


def update_rotation(obj, x, change_x, y, change_y, z, change_z):
    if change_x:
        obj.rotation_euler.x = math.radians(x)
    if change_y:
        obj.rotation_euler.y = math.radians(y)
    if change_z:
        obj.rotation_euler.z = math.radians(z)
    
    print('New object {} Rotation: {}, {}, {}'.format(obj.name, x, y, z))

def update_scale(obj, x, change_x, y, change_y, z, change_z):
    if change_x:
        obj.scale[0] = x

    if change_y:
        obj.scale[1] = y

    if change_z:
        obj.scale[2] = z

    print('New object {} Scale: {}, {}, {}'.format(obj.name, x, y, z))

for obj in selected_objects:

    update_location(obj, -10.305, False, 0, False, 5.1539, True)
    update_scale(obj, 0, False, 0, False, 0.15, True)
    #update_rotation(obj, 0, False, 0, False, rotation_z, False)
    #print(obj.rotation_axis_angle)
    print('--------------------------')
    
    