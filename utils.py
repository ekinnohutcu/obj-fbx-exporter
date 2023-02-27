import bpy
from . exlib import ShowMessageBox
from bpy.types import Operator

class Export_OT_operator(Operator):
    bl_idname = 'export.unity'
    bl_label = 'Export to Unity'
    
    bl_description = 'Export to Unity'
    bl_options = {"REGISTER", "UNDO"}

    def execute(self,context):
        
        export_mode = context.scene.my_tool.export_mode
        export_seperately = context.scene.my_tool.export_seperately
        
    
    
        context = bpy.context
        scene = context.scene
        viewlayer = context.view_layer


        obs = [o for o in scene.objects if o.type == 'MESH']
        bpy.ops.object.select_all(action='DESELECT')    

    
    
        if export_mode == 'OBJ':
            if(export_seperately):
                for ob in obs:
                    viewlayer.objects.active = ob
                    ob.select_set(True)
                    bpy.ops.export_scene.obj(
                    filepath=bpy.context.scene.directory + ob.name + '.fbx',
                    use_selection=True)
                    ob.select_set(False)
                # for obj in bpy.context.selected_objects:
                #     bpy.ops.export_scene.obj(filepath = bpy.context.scene.directory + obj.name + '.obj', use_selection = True)
            else:
                bpy.ops.export_scene.obj(filepath = bpy.context.scene.directory + bpy.context.scene.file_name + '.obj', use_selection = True)
        elif export_mode == 'FBX':
            if (export_seperately):
                for ob in obs:
                    viewlayer.objects.active = ob
                    ob.select_set(True)
                    bpy.ops.export_scene.fbx(filepath = bpy.context.scene.directory + ob.name + '.fbx', use_selection = True,apply_scale_options='FBX_SCALE_ALL',axis_forward='-Z',axis_up='Y',bake_space_transform = context.scene.my_tool.apply_transform,apply_unit_scale=True,use_space_transform=True,use_armature_deform_only=True,bake_anim = True,primary_bone_axis='Y',secondary_bone_axis='X',armature_nodetype='NULL',add_leaf_bones=False, bake_anim_use_nla_strips=True,bake_anim_use_all_bones=True,bake_anim_use_all_actions=True,bake_anim_force_startend_keying=True)
                    ob.select_set(False)
                # for obj in bpy.context.selected_objects:
                #    bpy.ops.export_scene.fbx(filepath = bpy.context.scene.directory + obj.name + '.fbx', use_selection = True,apply_scale_options='FBX_SCALE_ALL',axis_forward='-Z',axis_up='Y',bake_space_transform = context.scene.my_tool.apply_transform,apply_unit_scale=True,use_space_transform=True,use_armature_deform_only=True,bake_anim = True,primary_bone_axis='Y',secondary_bone_axis='X',armature_nodetype='NULL',add_leaf_bones=False, bake_anim_use_nla_strips=True,bake_anim_use_all_bones=True,bake_anim_use_all_actions=True,bake_anim_force_startend_keying=True)
            else:
                bpy.ops.export_scene.fbx(filepath = bpy.context.scene.directory + bpy.context.scene.file_name + '.fbx', use_selection = True,apply_scale_options='FBX_SCALE_ALL',axis_forward='-Z',axis_up='Y',bake_space_transform = context.scene.my_tool.apply_transform,apply_unit_scale=True,use_space_transform=True,use_armature_deform_only=True,bake_anim = True,primary_bone_axis='Y',secondary_bone_axis='X',armature_nodetype='NULL',add_leaf_bones=False, bake_anim_use_nla_strips=True,bake_anim_use_all_bones=True,bake_anim_use_all_actions=True,bake_anim_force_startend_keying=True)
        
        ShowMessageBox('Exported to Folder', 'Exported', 'INFO')
        return {'FINISHED'}
    
class MyProperties(bpy.types.PropertyGroup):
    
    export_mode: bpy.props.EnumProperty(name = 'Export Modes', items = [('OBJ', 'OBJ', ''), ('FBX', 'FBX', '')])
    apply_transform: bpy.props.BoolProperty(name = 'Apply Transform', default = True)
    export_seperately: bpy.props.BoolProperty(name = 'Export Seperately', default = False)
    
    