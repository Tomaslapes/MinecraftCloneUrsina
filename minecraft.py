from ursina import Ursina, Button, application,scene,Vec3,color,round_to_closest,mouse,destroy,lerp
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.ursinastuff import print_on_screen
from math import cos,sin
from perlin_noise import PerlinNoise

class Block(Button):
    def __init__(self,position_block):
        super().__init__(self,
        parent = scene,
        model = "Models/Cube.obj",
        texture = "Textures/CubeTex5.png",
        color = color.white,
        highlight_color = color.azure,
        origin = (0,0.5),
        position = position_block)
      
import numpy as np

noise = PerlinNoise(octaves=10, seed=1)

app = Ursina()


def input(key):
    if key ==  "left mouse down":
        destroy(mouse.hovered_entity)
        print_on_screen("Block destroyed")
    if key == "right mouse down":
        pass
    if key == "escape":
        application.quit()

blocks = []
for z in range(32):
    for x in range(32):
        y = noise([z/100,x/100])
        print(y)
        block = Block(Vec3(x,round_to_closest(y*10,1),z))
        blocks.append(block)

player = FirstPersonController(jump_duration = 0.25,jump_height = 1,gravity = 1)

app.run()