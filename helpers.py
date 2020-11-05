bl_info = {
    "name": "Node Menu Addons",
    "author": "Johnny Matthews",
    "version": (1, 1),
    "blender": (2, 80, 0),
    "location": "",
    "description": "",
    "warning": "",
    "wiki_url": "",
    "category": "Node",
}
import bpy

class NASeperateCombineRGB(bpy.types.Operator):
    """Add A Seperate and Combine RGB Node Pair connected together"""    
    bl_idname = "node.na_seperate_combine_rgb"
    bl_label = "Add Seperate / Combine RGBPair"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        snode = context.space_data
        return (snode.type == 'NODE_EDITOR')

    def execute(self, context):
  
        tree = context.space_data.node_tree
        bpy.ops.node.add_node(type="ShaderNodeSeparateRGB", use_transform=True)
        a = context.active_node
        bpy.ops.node.add_node(type="ShaderNodeCombineRGB", use_transform=True)
        b = context.active_node
        
        
        a.select = True
        b.location[0] = b.location[0]+200
        tree.links.new(a.outputs[0],b.inputs[0]) 
        tree.links.new(a.outputs[1],b.inputs[1]) 
        tree.links.new(a.outputs[2],b.inputs[2]) 
       
        return {'FINISHED'}


class NASeperateCombineXYZ(bpy.types.Operator):
    """Add A Seperate and Combine ZYX Node Pair connected together"""    
    bl_idname = "node.na_seperate_combine_xyz"
    bl_label = "Add Seperate / Combine XYZ Pair"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        snode = context.space_data
        return (snode.type == 'NODE_EDITOR')

    def execute(self, context):
  
        tree = context.space_data.node_tree
        bpy.ops.node.add_node(type="ShaderNodeSeparateXYZ")
        a = context.active_node
        bpy.ops.node.add_node(type="ShaderNodeCombineXYZ")
        b = context.active_node
        
        b.location[0] = b.location[0]+200        
        tree.links.new(a.outputs[0],b.inputs[0]) 
        tree.links.new(a.outputs[1],b.inputs[1]) 
        tree.links.new(a.outputs[2],b.inputs[2]) 
       
        a.select = True
       
        return {'FINISHED'}

class NASeperateCombineHSV(bpy.types.Operator):
    """Add A Seperate and Combine HSV Node Pair connected together"""    
    bl_idname = "node.na_seperate_combine_hsv"
    bl_label = "Add Seperate / Combine HSV Pair"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        snode = context.space_data
        return (snode.type == 'NODE_EDITOR')

    def execute(self, context):
  
        tree = context.space_data.node_tree
        bpy.ops.node.add_node(type="ShaderNodeSeparateHSV")
        a = context.active_node
        bpy.ops.node.add_node(type="ShaderNodeCombineHSV")
        b = context.active_node
        
        a.select = True
        b.location[0] = b.location[0]+200        
        tree.links.new(a.outputs[0],b.inputs[0]) 
        tree.links.new(a.outputs[1],b.inputs[1]) 
        tree.links.new(a.outputs[2],b.inputs[2]) 
       
        return {'FINISHED'}    


class NAVectorMath(bpy.types.Operator):
    """Add A Vector Math Node"""    
    bl_idname = "node.na_vector_math"
    bl_label = "Add Vector Math Node"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        snode = context.space_data
        return (snode.type == 'NODE_EDITOR')

    def execute(self, context):
        bpy.ops.node.add_node(type="ShaderNodeVectorMath")
        return {'FINISHED'} 





def converter_menu_func(self, context):
    col = self.layout.column(align=True)
    col.operator(NASeperateCombineRGB.bl_idname,text="RGB Seperate / Combine Pair")
    col.operator(NASeperateCombineXYZ.bl_idname,text="XYZ Seperate / Combine Pair")
    col.operator(NASeperateCombineHSV.bl_idname,text="HSV Seperate / Combine Pair")
    col.separator()

def vector_menu_func(self, context):
    col = self.layout.column(align=True)
    col.operator(NAVectorMath.bl_idname,text="Vector Math")
    col.separator()


def register():
    bpy.utils.register_class(NASeperateCombineRGB)
    bpy.utils.register_class(NASeperateCombineXYZ)
    bpy.utils.register_class(NASeperateCombineHSV)
    bpy.utils.register_class(NAVectorMath)
    bpy.types.NODE_MT_category_SH_NEW_CONVERTOR.prepend(converter_menu_func)
    bpy.types.NODE_MT_category_SH_NEW_OP_VECTOR.prepend(vector_menu_func)
    
    
def unregister():
    bpy.types.NODE_MT_category_SH_NEW_CONVERTOR.remove(converter_menu_func)
    bpy.types.NODE_MT_category_SH_NEW_OP_VECTOR.remove(vector_menu_func)
    bpy.utils.unregister_class(NASeperateCombineRGB)
    bpy.utils.unregister_class(NASeperateCombineXYZ)
    bpy.utils.unregister_class(NASeperateCombineHSV)
    bpy.utils.unregister_class(NAVectorMath)

if __name__ == "__main__":
    register()
