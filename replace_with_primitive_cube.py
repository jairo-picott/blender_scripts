import bpy

custom_name = "AutomaticDoor[15270631]"
use_custom_name = False

def create_cube_and_hide(obj):
    dimensions = obj.dimensions

    #Adding a primitive cube with size 1 and the selected object location
    bpy.ops.mesh.primitive_cube_add(size=1, location=obj.location)

    #selecting the newly created cube and set the data as the selected element
    cube = bpy.context.active_object
    cube.dimensions = dimensions

    if use_custom_name:
        cube.name = custom_name
    else:
        cube.name = "c{}".format(obj.name)
    #cube.name_full = "c{}".format(obj.name_full)
    cube.rotation_axis_angle = obj.rotation_axis_angle

    #Hide the original
    obj.hide_set(True)


if bpy.context.selected_objects:

    for obj in bpy.context.selected_objects:
        if obj.type == "MESH":
            create_cube_and_hide(obj)


    
    print("Done")
    
else:
    print("No active mesh object selected.")