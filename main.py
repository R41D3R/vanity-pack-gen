import glob
import json
import os
from PIL import Image 

from tool_json import create_base_dict, create_design_model, create_skin_model

PACK_NAME = "test_pack"
design_path = f"data/{PACK_NAME}/vanity/designs"
texture_path = f"assets/{PACK_NAME}/textures/item"
lang_path = f"assets/{PACK_NAME}/lang"
models_path = f"assets/{PACK_NAME}/models/item/vanity"

# design for every texture
os.makedirs(design_path, exist_ok=True)
os.makedirs(texture_path, exist_ok=True)
os.makedirs(lang_path, exist_ok=True)
os.makedirs(models_path, exist_ok=True)

input_files = glob.glob('input/*.png')

for file_path in input_files:
    
    file_name = file_path[:-4].split("/")[1].split("_")
    tool_type = file_name[1]
    skin_name = file_name[0] 
    print(tool_type, skin_name)
    design_model_name = f"{tool_type}_{skin_name}_design"
    skin_model_name = f"{tool_type}_{skin_name}"

    # create design jsons
    design_json = create_base_dict(PACK_NAME, design_model_name, skin_model_name, tool_type)
    save_path = f"{design_path}/{tool_type}_{skin_name}.json"
    with open(save_path, 'w') as f:
        json.dump(design_json, f, indent=4)

    # create models
    with open(f"{models_path}/{design_model_name}.json", "w") as f:
        json.dump(create_design_model(PACK_NAME, design_model_name), f, indent=4)
    with open(f"{models_path}/{skin_model_name}.json", "w") as f:
        json.dump(create_skin_model(PACK_NAME, skin_model_name), f, indent=4)

    

    # edit images
    
    # Back Image 
    filename1 = 'token_base.png'
    
    # Open Front Image 
    frontImage = Image.open(file_path) 
    
    # Open Background Image 
    background = Image.open(filename1) 
    
    # Convert image to RGBA 
    frontImage = frontImage.convert("RGBA") 
    
    # Convert image to RGBA 
    background = background.convert("RGBA") 
    
    # Calculate width to be at the center 
    width = (background.width - frontImage.width) // 2
    
    # Calculate height to be at the center 
    height = (background.height - frontImage.height) // 2
    
    # Paste the frontImage at (width, height) 
    background.paste(frontImage, (width, height), frontImage) 
    
    # Save this image 
    background.save(f"{texture_path}/{design_model_name}.png", format="png")
    frontImage.save(f"{texture_path}/{skin_model_name}.png", format="png")



    





