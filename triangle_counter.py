import bpy
import os

def triangle_count(obj):
    mesh = obj.data
    return sum(len(p.vertices) - 2 for p in mesh.polygons)

#mesh_objects = [obj for obj bpy.context.scene.objects if obj.type == 'MESH']

file_path = './temp/triangle_count.txt'

mesh_objects = []

from_collection = True

if from_collection:
    print('From collection')
    collection_name = "L1"
    collection = bpy.data.collections.get(collection_name)

    if collection:
        for obj in collection.objects:
            mesh_objects.append(obj)
    else:
        print("!!!Not valid collection name!!!")
        exit()
else:
    print('All objects')
    for obj in bpy.context.scene.objects:
        if obj.type == 'MESH':
            mesh_objects.append(obj)


tri_count_list = [(obj, triangle_count(obj)) for obj in mesh_objects]

tri_count_list.sort(key=lambda x: x[1], reverse=True)

with open(file_path, 'w') as file:
    
    for obj, count in tri_count_list:
        file.write("{}: {} triangles\n".format(obj.name, count))


print("Done")