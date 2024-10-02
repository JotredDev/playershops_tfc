
from PIL import Image
import numpy as np


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



def swap_texture () :

    base_texture = Image.open("base/base_texture.png")
    base_texture = base_texture.convert ("RGBA")
    np_base_texture = np.array(base_texture)

    for wood in wood_types :
        
        wood_inner = Image.open("base/inner/" + wood + ".png")
        wood_inner = wood_inner.convert ("RGBA")
        np_wood_inner = np.array(wood_inner)

        for i in range(1, 15) :

            for j in range (1, 15) :

                np_base_texture[i + 16, j] = np_wood_inner[i, j]

        
        wood_outer = Image.open("base/outer/" + wood + ".png")
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
        texture.save("player_shops/" + wood + ".png")



def __main__ () :

    swap_texture ()


if __name__ == "__main__" :
    __main__ ()

