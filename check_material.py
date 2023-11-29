import bpy


collection_name = "L1"
collection = bpy.data.collections.get(collection_name)

count = 0


if collection:
    objects = collection.objects
    total = len(objects)

    for obj in objects:
        if not obj.data.materials:
            print("!!------")
            print("The object {} has no materials associated.".format(obj.name))
            print("--------")
            count = count + 1
        else:
            #Hide
            #obj.hide_set(False)
            ...
    
    print("Missing {} from {} element for material to be assigned!.".format(count, total))
else:
    print("Please select a valid collection.")