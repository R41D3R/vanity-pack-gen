TOOL_MATERIAL_NAMES = ["wooden", "stone", "golden", "iron", "diamond", "netherite"]


item_type_lists = {
    "sword": [f"{material}_sword" for material in TOOL_MATERIAL_NAMES],
    "axe": [f"{material}_axe" for material in TOOL_MATERIAL_NAMES],
    "pickaxe": [f"{material}_pickaxe" for material in TOOL_MATERIAL_NAMES],
    "shovel": [f"{material}_shovel" for material in TOOL_MATERIAL_NAMES],
    "hoe": [f"{material}_hoe" for material in TOOL_MATERIAL_NAMES],
}
SWORDS = [f"{material}_sword" for material in TOOL_MATERIAL_NAMES]
AXES = [f"{material}_axe" for material in TOOL_MATERIAL_NAMES]
PICKAXES = [f"{material}_pickaxe" for material in TOOL_MATERIAL_NAMES]
SHOVELS = [f"{material}_shovel" for material in TOOL_MATERIAL_NAMES]
HOES = [f"{material}_hoe" for material in TOOL_MATERIAL_NAMES]



def create_base_dict(design_pack_name, design_model_name, skin_model_name, tool_type):
   
    return {
        "model": f"{design_pack_name}:{design_model_name}", # model for design holding item
        "type": "sellable",
        "styles": {
            "default": [{
                "item": f"minecraft:{item}",
                "asset": {
                    "default": f"{design_pack_name}:{skin_model_name}",
                    "hand": f"{design_pack_name}:{skin_model_name}"
                }
                } for item in item_type_lists[tool_type]]
        }
    }


def create_design_model(design_pack_name, design_texture_name):

    return {
        "parent": "minecraft:item/generated",
        "textures": {
            "layer0": f"{design_pack_name}:item/{design_texture_name}"
        }
    }


def create_skin_model(design_pack_name, skin_texture_name):
    return {
        "parent": "vanity:item/handheld_item",
        "textures": {
            "layer0": f"{design_pack_name}:item/{skin_texture_name}"
        }
    }
