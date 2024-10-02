
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
    recipe_file.write ("  \"ingredient\": [\n")
    recipe_file.write ("    \"item\": \"tfc:wood/sign/%s\"\n" % wood)
    recipe_file.write ("  },\n")
    recipe_file.write ("  \"size\": \"large\",\n")
    recipe_file.write ("  \"weight\": \"heavy\",\n")
    recipe_file.write ("}")

    recipe_file.close ()

    return


def write_all () :

    # The program automatically writes tag files for all metals
    for wood in wood_types :

        write_model (wood)
    
    return



def __main__ () :

    write_all ()


if __name__ == "__main__" :
    __main__ ()
