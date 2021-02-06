from ursina import Ursina, Button, application,scene,Vec3,color,round_to_closest,mouse,destroy,lerp,held_keys,Sky,Entity,DirectionalLight
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.ursinastuff import print_on_screen
from ursina.shaders import lit_with_shadows_shader

from math import cos,sin
from perlin_noise import PerlinNoise
from random import randrange

PLAYER_SPEED = 5
PAYER_RUN_SPEED = 8

class Block(Button):
    def __init__(self,position_block,texture = "Textures/CubeTex5.png"):
        super().__init__(self,
        parent = scene,
        shader=lit_with_shadows_shader,
        model = "Models/Cube.obj",
        texture = texture,
        color = color.white,
        highlight_color = color.gray,
        origin = (0,0.5),
        position = position_block)

class Tree():
    def __init__(self,position,height,num_of_leaves,texture = "Textures/Wood2.png"):
        base = []
        for i in range(height):
            block = Block((position[0],position[1]+i,position[2]),texture)
        #for leave in range(num_of_leaves):
        x = position[0]
        z = position[2]
        y = position[1]+height
        leaves_tex = "Textures/Leaves.jpg"
        Block((x,y,z),leaves_tex)
        Block((x+1,y,z),leaves_tex)
        Block((x-1,y,z),leaves_tex)
        Block((x,y,z+1),leaves_tex)
        Block((x,y,z-1),leaves_tex)
        Block((x,y+1,z),leaves_tex)


noise = PerlinNoise(octaves=10, seed=1)

app = Ursina()

sky = Sky()

sun = DirectionalLight(y=2, z=3, shadows=True,shadow_map_resolution = (1024,1024))
sun.rotation = (45,45,0)


def input(key):
    if key ==  "left mouse down":
        destroy(mouse.hovered_entity)
        print_on_screen("Block destroyed")
    if key == "right mouse down":
        pass
    if key == "escape":
        application.quit()
    if held_keys["shift"]:
        player.speed = PAYER_RUN_SPEED
        print_on_screen("Run")
    else:
        player.speed = PLAYER_SPEED
        print_on_screen("Walk")

blocks = []
for z in range(32):
    for x in range(32):
        
        y = noise([z/100,x/100])
        y = round_to_closest(y*10,1)

        tree_ = randrange(0,100)
        if tree_ % 20 == 0:
            Tree((x,y+1,z),4,10)
        print(y)
        block = Block(Vec3(x,y,z))
        blocks.append(block)



player = FirstPersonController(jump_duration = 0.25,jump_height = 1,gravity = 1)

app.run()