import bpy

def decimate_obj(obj, ratio):
    print('The objects selected will be decimated with ratio {}'.format(ratio))
    mod = obj.modifiers.new(name = 'DecimateMod', type='DECIMATE')
    mod.ratio = ratio
    print('Done for object {}'.format(obj.name))
    print('----')

if bpy.context.selected_objects:
    for obj in bpy.context.selected_objects:
        if obj.type == "MESH":
            decimate_obj(obj, 0.25)
            #obj.modifiers.active()
        else:
            print("!!!The object {} is not of type MESH!!!".format(obj.name))
    
else:
    print("!!!Must be selected at least one element.!!!")