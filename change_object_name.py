import bpy


def change_object_name(obj, new_name):
    if obj.type == "MESH":
        old_name = obj.name
        obj.name = new_name
        print("Name changed from {} --> to {}".format(old_name, new_name))




#get selected objects

selected_objects = bpy.context.selected_objects

ids = [13581025]


index = 0
for id in ids:
    new_name = "Door[{}]".format(id)
    change_object_name(selected_objects[index], new_name)
    index = index + 1


