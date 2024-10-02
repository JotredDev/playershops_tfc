
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

message = """  },
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







def write_model (wood : str) :

    block_model_file = open ("models/block/wood/player_shops/" + wood + ".json", "wt")


    block_model_file.write ("{\n")
    block_model_file.write ("  \"credit\": \"Made with Blockbench\",\n")
    block_model_file.write ("  \"render_type\": \"minecraft:cutout\",")
    block_model_file.write ("  \"textures\": {\n")
    block_model_file.write ("    \"0\": \"playershops_tfc:block/wood/player_shops/%s\",\n" % wood)
    block_model_file.write ("    \"particle\": \"playershops_tfc:block/wood/player_shops/%s\"\n" % wood)
    block_model_file.write (message)


    block_model_file.close ()


    item_model_file = open ("models/item/wood/player_shops/" + wood + ".json", "wt")

    item_model_file.write ("{\n")
    item_model_file.write ("  \"parent\": \"playershops_tfc:block/wood/player_shops/%s\"\n" % wood)
    item_model_file.write ("}\n")

    item_model_file.close ()


    blockstate_model_file = open ("blockstates/wood/player_shops/" + wood + ".json", "wt")

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


def write_all () :

    # The program automatically writes tag files for all woods
    for wood in wood_types :

        write_model (wood)
    
    return



def __main__ () :

    write_all ()


if __name__ == "__main__" :
    __main__ ()
