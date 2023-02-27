import bpy
from bpy.types import Panel

class Exporter_Panel(Panel):
    bl_idname = 'EXPORTER_PT_eToolSet'
    bl_label = 'Exporter Panel'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Exporter'
    
    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.prop(context.scene.my_tool, 'export_seperately', text = 'Export Seperately')
        row = layout.row()
        row.prop(context.scene.my_tool, 'export_mode', expand = True)
        row = layout.row()
        row.prop(context.scene, 'file_name', text = 'File Name')
        row = layout.row()
        row.prop(context.scene, 'directory', text = 'Directory')
        row = layout.row()
        row.prop(context.scene.my_tool, 'apply_transform', text = 'Apply Transform')
        row = layout.row()
        row.operator('export.unity', text = 'Export to Folder')