bl_info = {
    "name" : "unity-exporter",
    "author" : "ekin-nohutcu",
    "description" : "",
    "blender" : (3, 3, 1),
    "version" : (0, 0, 1),
    "location" : "",
    "warning" : "",
    "category" : "Tools"
}

import bpy
import os
from bpy.props import PointerProperty
from . utils import MyProperties, Export_OT_operator
from . panel import Exporter_Panel

classes = (MyProperties, Export_OT_operator, Exporter_Panel)

def register():
    from bpy.utils import register_class

    for cls in classes:
      register_class(cls)
      
    bpy.types.Scene.my_tool = bpy.props.PointerProperty(type = MyProperties)
    bpy.types.Scene.directory = bpy.props.StringProperty(name = 'blender_export_file_directory', subtype='DIR_PATH',default='')
    bpy.types.Scene.file_name = bpy.props.StringProperty(name = 'blender_export_file_name', default='')
    
    
def unregister():
    from bpy.utils import register_class

    for cls in reversed(classes):
      unregister(cls)

if __name__ == "__main__":
    register()