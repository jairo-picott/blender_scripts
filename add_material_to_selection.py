import bpy

#material = bpy.data.materials.new(name="Steel")
material = bpy.data.materials.get("Steel")

if bpy.context.selected_objects:
    for obj in bpy.context.selected_objects:
        if obj.type == "MESH":

            if not obj.data.materials:
                obj.data.materials.append(material)
                print("Material {} added to {}.".format(material.name, obj.name))
            else:
                obj.data.materials[0] = material
                print("Existing material in {} was replaced for {}.".format(obj.name, material.name))

        else:
            print("{} is not of type MESH.".format(obj.name))
else:
    print("Please select at least one element.")

    