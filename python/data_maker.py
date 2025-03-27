
import os


from PIL import Image
import numpy as np

tfc_wood_types = [
    "acacia",
    "ash",
    "aspen",
    "birch",
    "blackwood",
    "chestnut",
    "douglas_fir",
    "hickory",
    "kapok",
    "mangrove",
    "maple",
    "oak",
    "palm",
    "pine",
    "rosewood",
    "sequoia",
    "spruce",
    "sycamore",
    "white_cedar",
    "willow"
]

afc_wood_types = [
    "baobab",
    "eucalyptus",
    "mahogany",
    "hevea",
    "tualang",
    "teak",
    "cypress",
    "fig",
    "ironwood",
    "ipe"
]





model_content = """  },
  \"elements\": [
    {
      \"name\": \"Base1\",
      \"from\": [1, 0, 1],
      \"to\": [15, 2, 15],
      \"faces\": {
        \"north\": {\"uv\": [0.5, 7, 7.5, 8], \"texture\": \"#0\"},
        \"east\": {\"uv\": [0.5, 7, 7.5, 8], \"texture\": \"#0\"},
        \"south\": {\"uv\": [0.5, 7, 7.5, 8], \"texture\": \"#0\"},
        \"west\": {\"uv\": [0.5, 7, 7.5, 8], \"texture\": \"#0\"},
        \"up\": {\"uv\": [0.5, 8.5, 7.5, 15.5], \"texture\": \"#0\"},
        \"down\": {\"uv\": [0.5, 8.5, 7.5, 15.5], \"texture\": \"#0\"}
      }
    },
    {
      \"name\": \"Base2\",
      \"from\": [2, 2, 2],
      \"to\": [14, 3, 14],
      \"faces\": {
        \"north\": {\"uv\": [1, 6.5, 7, 7], \"texture\": \"#0\"},
        \"east\": {\"uv\": [1, 6.5, 7, 7], \"texture\": \"#0\"},
        \"south\": {\"uv\": [1, 6.5, 7, 7], \"texture\": \"#0\"},
        \"west\": {\"uv\": [1, 6.5, 7, 7], \"texture\": \"#0\"},
        \"up\": {\"uv\": [1, 9, 7, 15], \"texture\": \"#0\"},
        \"down\": {\"uv\": [1, 9, 7, 15], \"texture\": \"#0\"}
      }
    },
    {
      \"name\": \"GlassCase\",
      \"from\": [3, 3, 3],
      \"to\": [13, 13, 13],
      \"faces\": {
        \"north\": {\"uv\": [9.5, 9.5, 14.5, 14.5], \"texture\": \"#0\"},
        \"east\": {\"uv\": [9.5, 9.5, 14.5, 14.5], \"texture\": \"#0\"},
        \"south\": {\"uv\": [9.5, 9.5, 14.5, 14.5], \"texture\": \"#0\"},
        \"west\": {\"uv\": [9.5, 9.5, 14.5, 14.5], \"texture\": \"#0\"},
        \"up\": {\"uv\": [9.5, 9.5, 14.5, 14.5], \"texture\": \"#0\"},
        \"down\": {\"uv\": [9.5, 2, 14.5, 7], \"texture\": \"#0\"}
      }
    },
    {
      \"name\": \"Lable\",
      \"from\": [4, 0, 0],
      \"to\": [12, 4, 2],
      \"faces\": {
        \"north\": {\"uv\": [2, 4, 6, 6], \"texture\": \"#0\"},
        \"east\": {\"uv\": [0.5, 4, 1.5, 6], \"texture\": \"#0\"},
        \"south\": {\"uv\": [2, 4, 6, 6], \"texture\": \"#0\"},
        \"west\": {\"uv\": [0.5, 4, 1.5, 6], \"texture\": \"#0\"},
        \"up\": {\"uv\": [2, 2.5, 6, 3.5], \"texture\": \"#0\"},
        \"down\": {\"uv\": [2, 2, 6, 3], \"texture\": \"#0\"}
      }
    }
  ],
  \"display\": {
    \"thirdperson_righthand\": {
      \"rotation\": [75, 45, 0],
      \"translation\": [0, 2.5, 0],
      \"scale\": [0.375, 0.375, 0.375]
    },
    \"thirdperson_lefthand\": {
      \"rotation\": [75, 45, 0],
      \"translation\": [0, 2.5, 0],
      \"scale\": [0.375, 0.375, 0.375]
    },
    \"firstperson_righthand\": {
      \"rotation\": [0, 45, 0],
      \"scale\": [0.4, 0.4, 0.4]
    },
    \"firstperson_lefthand\": {
      \"rotation\": [0, 225, 0],
      \"scale\": [0.4, 0.4, 0.4]
    },
    \"ground\": {
      \"translation\": [0, 3, 0],
      \"scale\": [0.25, 0.25, 0.25]
    },
    \"gui\": {
      \"rotation\": [30, 225, 0],
      \"scale\": [0.625, 0.625, 0.625]
    },
    \"head\": {
      \"translation\": [0, 14.25, 0]
    },
    \"fixed\": {
      \"scale\": [0.5, 0.5, 0.5]
    }
  }
}
"""


def write_recipe (wood : str, path : str, wood_source : str) :

    recipe_file = open (path + "recipes\\crafting\\wood\\player_shops\\" + wood + ".json", "wt")

    recipe_file.write ("{\n")

    # For non-TFC wood types, the recipe is only loaded if the respective addon is loaded
    if wood_source != "tfc" :

      recipe_file.write ("\"conditions\": [\n")
      recipe_file.write ("  {\n")
      recipe_file.write ("    \"type\": \"forge:mod_loaded\",\n")
      recipe_file.write ("    \"modid\": \"%s\"\n" % wood_source)
      recipe_file.write ("  }\n")
      recipe_file.write ("],\n")

    recipe_file.write ("  \"type\": \"minecraft:crafting_shaped\",\n")
    recipe_file.write ("  \"pattern\": [\n")
    recipe_file.write ("    \" G \",\n")
    recipe_file.write ("    \"WSW\",\n")
    recipe_file.write ("    \"WWW\"\n")
    recipe_file.write ("  ],\n")
    recipe_file.write ("  \"key\": {\n")
    recipe_file.write ("    \"G\": {\n")
    recipe_file.write ("      \"tag\": \"forge:glass\"\n")
    recipe_file.write ("    },\n")
    recipe_file.write ("    \"S\": {\n")
    recipe_file.write ("      \"item\": \"%s:wood/sign/%s\"\n" % (wood_source, wood))
    recipe_file.write ("    },\n")
    recipe_file.write ("    \"W\": {\n")
    recipe_file.write ("      \"item\": \"%s:wood/stripped_wood/%s\"\n" % (wood_source, wood))
    recipe_file.write ("    }\n")
    recipe_file.write ("  },\n")
    recipe_file.write ("  \"result\": {\n")
    recipe_file.write ("    \"item\": \"playershops_tfc:wood/player_shops/%s\"\n" % wood)
    recipe_file.write ("  }\n")
    recipe_file.write ("}")

    recipe_file.close ()

    return

def write_texture (wood_types : list, path : str, base_path : str) :

    base_texture = Image.open("base\\base_texture.png")
    base_texture = base_texture.convert ("RGBA")
    np_base_texture = np.array(base_texture)

    for wood in wood_types :
        
        wood_inner = Image.open("base\\inner\\" + wood + ".png")
        wood_inner = wood_inner.convert ("RGBA")
        np_wood_inner = np.array(wood_inner)

        for i in range(1, 15) :

            for j in range (1, 15) :

                np_base_texture[i + 16, j] = np_wood_inner[i, j]

        
        wood_outer = Image.open("base\\outer\\" + wood + ".png")
        wood_outer = wood_outer.convert ("RGBA")
        np_wood_outer = np.array(wood_outer)

        for i in range (3) :

            for j in range (1, 15) :

                np_base_texture[i + 13, j] = np_wood_outer[i, j]

        for i in range (4) :

            for j in range (1, 3) :

                np_base_texture[i + 8, j] = np_wood_outer[i, j]
                
        for i in range (4) :

            for j in range (4, 12) :

                np_base_texture[i + 8, j] = np_wood_outer[i, j]
                
        for i in range (2) :

            for j in range (4, 12) :

                np_base_texture[i + 5, j] = np_wood_outer[j, i + 13]


        texture = Image.fromarray(np_base_texture)
        texture.save(path + "textures\\block\\wood\\player_shops\\" + wood + ".png")
    
    return

def write_model (wood : str, path : str) :

    block_model_file = open (path + "models\\block\\wood\\player_shops\\" + wood + ".json", "wt")


    block_model_file.write ("{\n")
    block_model_file.write ("  \"credit\": \"Made with Blockbench\",\n")
    block_model_file.write ("  \"render_type\": \"minecraft:cutout\",")
    block_model_file.write ("  \"textures\": {\n")
    block_model_file.write ("    \"0\": \"playershops_tfc:block/wood/player_shops/%s\",\n" % wood)
    block_model_file.write ("    \"particle\": \"playershops_tfc:block/wood/player_shops/%s\"\n" % wood)
    block_model_file.write (model_content)


    block_model_file.close ()


    item_model_file = open (path + "models\\item\\wood\\player_shops\\" + wood + ".json", "wt")

    item_model_file.write ("{\n")
    item_model_file.write ("  \"parent\": \"playershops_tfc:block/wood/player_shops/%s\"\n" % wood)
    item_model_file.write ("}\n")

    item_model_file.close ()


    blockstate_model_file = open (path + "blockstates\\wood\\player_shops\\" + wood + ".json", "wt")

    blockstate_model_file.write ("{\n")
    blockstate_model_file.write ("  \"variants\": {\n")
    blockstate_model_file.write ("    \"facing=north\": { \"model\": \"playershops_tfc:block/wood/player_shops/%s\" },\n" % wood)
    blockstate_model_file.write ("    \"facing=east\": { \"model\": \"playershops_tfc:block/wood/player_shops/%s\", \"y\": 90 },\n" % wood)
    blockstate_model_file.write ("    \"facing=south\": { \"model\": \"playershops_tfc:block/wood/player_shops/%s\", \"y\": 180 },\n" % wood)
    blockstate_model_file.write ("    \"facing=west\": { \"model\": \"playershops_tfc:block/wood/player_shops/%s\", \"y\": 270 }\n" % wood)
    blockstate_model_file.write ("  }\n")
    blockstate_model_file.write ("}")

    blockstate_model_file.close ()

    return

def write_tags (wood_types : list, addon_wood_types : list, path : str) :

    # Item tags
    item_tag_file = open (path + "tags\\items\\playershop.json", "wt")
    
    item_tag_file.write ("{\n")
    item_tag_file.write ("  \"replace\": false,\n")
    item_tag_file.write ("  \"values\": [\n")

    #Base wood
    for wood in wood_types :

        item_tag_file.write ("    \"playershops_tfc:wood/player_shops/%s\",\n" % wood)

    # Addon wood
    for i in range (len (addon_wood_types) - 1) :
        
        item_tag_file.write ("    {\n")
        item_tag_file.write ("      \"id\": \"playershops_tfc:wood/player_shops/%s\",\n" % addon_wood_types[i])
        item_tag_file.write ("      \"required\": false\n")
        item_tag_file.write ("    },\n")
    
    item_tag_file.write ("    {\n")
    item_tag_file.write ("      \"id\": \"playershops_tfc:wood/player_shops/%s\",\n" % addon_wood_types[-1])
    item_tag_file.write ("      \"required\": false\n")
    item_tag_file.write ("    }\n")

    item_tag_file.write ("  ]\n")
    item_tag_file.write ("}")

    item_tag_file.close ()

    # Block tags
    block_tag_file = open (path + "tags\\blocks\\playershop.json", "wt")
    
    block_tag_file.write ("{\n")
    block_tag_file.write ("  \"replace\": false,\n")
    block_tag_file.write ("  \"values\": [\n")

    #Base wood
    for wood in wood_types :

        block_tag_file.write ("    \"playershops_tfc:wood/player_shops/%s\",\n" % wood)

    # Addon wood
    for i in range (len (addon_wood_types) - 1) :
        
        block_tag_file.write ("    {\n")
        block_tag_file.write ("      \"id\": \"playershops_tfc:wood/player_shops/%s\",\n" % addon_wood_types[i])
        block_tag_file.write ("      \"required\": false\n")
        block_tag_file.write ("    },\n")
    
    block_tag_file.write ("    {\n")
    block_tag_file.write ("      \"id\": \"playershops_tfc:wood/player_shops/%s\",\n" % addon_wood_types[-1])
    block_tag_file.write ("      \"required\": false\n")
    block_tag_file.write ("    }\n")

    block_tag_file.write ("  ]\n")
    block_tag_file.write ("}")

    block_tag_file.close ()

    return

def readable_name (wood : str) :

    output = wood.replace ('_', ' ')
    output = list (output)
    output[0] = output[0].upper ()

    for i in range (len (output)) :

        if output[i] == ' ' :
            output[i + 1] = output[i + 1].upper ()

    return "".join (output)


def write_en_us_lang (wood_types : list, addon_wood_types : list, path : str) :

    lang_file = open (path + "lang\\en_us.json", "wt")
    
    lang_file.write ("{\n")

    for wood in wood_types :

        lang_file.write ("  \"block.playershops_tfc.wood.player_shops.%s\": \"%s Player Shop\",\n" % (wood, readable_name (wood)))
    
    for wood in addon_wood_types :

        lang_file.write ("  \"block.playershops_tfc.wood.player_shops.%s\": \"%s Player Shop\",\n" % (wood, readable_name (wood)))

    lang_file.write ("  \"playershops_tfc.creative_tab.playershops\": \"Player Shops TFC\"\n")
    lang_file.write ("}")



    return








def write_all (wood_types : list, modID : str, wood_source) :

    # Preparing the directory paths for data and assets
    base_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'src'))
    data_path = base_path + "\\main\\resources\\data\\%s\\" % modID
    assets_path = base_path + "\\main\\resources\\assets\\%s\\" % modID

    # List of all non-base wood types
    # If more wood addons are made, add their wood to this list
    all_addon_wood_types = afc_wood_types

    for wood in wood_types :

        write_recipe (wood, data_path, wood_source)
        write_texture (wood_types, assets_path, base_path)
        write_model (wood, assets_path)
        write_tags (tfc_wood_types, all_addon_wood_types, base_path + "\\main\\resources\\data\\playershops\\")
        write_en_us_lang (tfc_wood_types, all_addon_wood_types, assets_path)

    return



def __main__ () :

    base = "playershops_tfc"

    write_all (tfc_wood_types, base, "tfc")
    write_all (afc_wood_types, base, "afc")


if __name__ == "__main__" :
    __main__ ()
