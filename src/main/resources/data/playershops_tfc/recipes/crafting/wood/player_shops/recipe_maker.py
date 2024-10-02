
wood_types = [
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

def write_model (wood : str) :

    recipe_file = open (wood + ".json", "wt")

    recipe_file.write ("{\n")
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
    recipe_file.write ("      \"item\": \"tfc:wood/sign/%s\"\n" % wood)
    recipe_file.write ("    },\n")
    recipe_file.write ("    \"W\": {\n")
    recipe_file.write ("      \"item\": \"tfc:wood/stripped_wood/%s\"\n" % wood)
    recipe_file.write ("    }\n")
    recipe_file.write ("  },\n")
    recipe_file.write ("  \"result\": {\n")
    recipe_file.write ("    \"item\": \"playershops_tfc:wood/player_shops/%s\"\n" % wood)
    recipe_file.write ("  }\n")
    recipe_file.write ("}")

    recipe_file.close ()

    return


def write_all () :

    # The program automatically writes tag files for all woods
    for wood in wood_types :

        write_model (wood)
    
    return



def __main__ () :

    write_all ()


if __name__ == "__main__" :
    __main__ ()
