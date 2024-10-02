
wood_types = [
    "acacia",
    "bamboo",
    "birch",
    "cherry",
    "crimson",
    "dark_oak",
    "jungle",
    "mangrove",
    "oak",
    "spruce",
    "warped"
]

def write_model (wood : str) :

    recipe_file = open (wood + "_player_shop.json", "wt")

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
    recipe_file.write ("      \"item\": \"minecraft:%s_sign\"\n" % wood)
    recipe_file.write ("    },\n")
    recipe_file.write ("    \"W\": {\n")
    recipe_file.write ("      \"item\": \"minecraft:stripped_%s_log\"\n" % wood)
    recipe_file.write ("    }\n")
    recipe_file.write ("  },\n")
    recipe_file.write ("  \"result\": {\n")
    recipe_file.write ("    \"count\": 0,")
    recipe_file.write ("    \"item\": \"playershops:%s_player_shop\"\n" % wood)
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
