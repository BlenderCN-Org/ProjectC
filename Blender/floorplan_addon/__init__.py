import bpy

bl_info = {
    "name" : "Import Floor Plan",
    "author" : "Pedro Bronsveld",
    "description" : "Import HR floor plans.",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 1),
    "location" : "View3D",
    "warning" : "",
    "category" : "Import-Export"
}

from . FloorplanImporter import FloorplanImporter
from . FloorplanExporter import FloorplanExporter
from . FloorplanTools import *


# Only needed if you want to add into a dynamic menu
def menu_func_import(self, context):
    self.layout.operator(FloorplanImporter.bl_idname, text="HR Floor Plan")

def menu_func_export(self, context):
    self.layout.operator(FloorplanExporter.bl_idname, text="HR Floor Plan")

def register():
    bpy.utils.register_class(FloorplanImporter)
    bpy.types.TOPBAR_MT_file_import.append(menu_func_import)
    bpy.utils.register_class(FloorplanExporter)
    bpy.types.TOPBAR_MT_file_export.append(menu_func_export)

    bpy.utils.register_class(AlignFloors)
    bpy.utils.register_class(HideReferenceImages)
    bpy.utils.register_class(ShowReferenceImages)
    bpy.utils.register_class(HideRoomNodes)
    bpy.utils.register_class(ShowRoomNodes)
    bpy.utils.register_class(CreateWalls)
    bpy.utils.register_class(CreateNode)
    bpy.utils.register_class(ConnectNodesToRooms)
    bpy.utils.register_class(ConnectRoomsToNodes)
    bpy.utils.register_class(RemoveWalls)

    bpy.utils.register_class(FloorplanToolsPanel)


def unregister():
    bpy.utils.unregister_class(FloorplanImporter)
    bpy.types.TOPBAR_MT_file_import.remove(menu_func_import)
    bpy.utils.unregister_class(FloorplanExporter)
    bpy.types.TOPBAR_MT_file_export.remove(menu_func_export)

    bpy.utils.unregister_class(AlignFloors)
    bpy.utils.unregister_class(HideReferenceImages)
    bpy.utils.unregister_class(ShowReferenceImages)
    bpy.utils.unregister_class(HideRoomNodes)
    bpy.utils.unregister_class(ShowRoomNodes)
    bpy.utils.unregister_class(CreateWalls)
    bpy.utils.unregister_class(CreateNode)
    bpy.utils.unregister_class(ConnectNodesToRooms)
    bpy.utils.unregister_class(ConnectRoomsToNodes)
    bpy.utils.unregister_class(RemoveWalls)

    bpy.utils.unregister_class(FloorplanToolsPanel)


if __name__ == "__main__":
    register()

    # test call
    bpy.ops.import_test.some_data('INVOKE_DEFAULT')