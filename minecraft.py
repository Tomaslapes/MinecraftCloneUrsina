from ursina import Ursina, Button, application,scene,Vec3,color,round_to_closest,mouse,destroy,lerp
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.ursinastuff import print_on_screen
from math import cos,sin

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

noise = [151, 160, 137, 91, 90, 15, 131, 13, 201, 95, 96, 53, 194, 233, 7, 225, 140, 36, 
                      103, 30, 69, 142, 8, 99, 37, 240, 21, 10, 23, 190, 6, 148, 247, 120, 234, 75, 0, 
                      26, 197, 62, 94, 252, 219, 203, 117, 35, 11, 32, 57, 177, 33, 88, 237, 149, 56, 
                      87, 174, 20, 125, 136, 171, 168, 68, 175, 74, 165, 71, 134, 139, 48, 27, 166, 
                      77, 146, 158, 231, 83, 111, 229, 122, 60, 211, 133, 230, 220, 105, 92, 41, 55, 
                      46, 245, 40, 244, 102, 143, 54, 65, 25, 63, 161, 1, 216, 80, 73, 209, 76, 132, 
                      187, 208, 89, 18, 169, 200, 196, 135, 130, 116, 188, 159, 86, 164, 100, 109, 
                      198, 173, 186, 3, 64, 52, 217, 226, 250, 124, 123, 5, 202, 38, 147, 118, 126, 
                      255, 82, 85, 212, 207, 206, 59, 227, 47, 16, 58, 17, 182, 189, 28, 42, 223, 183, 
                      170, 213, 119, 248, 152, 2, 44, 154, 163, 70, 221, 153, 101, 155, 167, 43, 
                      172, 9, 129, 22, 39, 253, 19, 98, 108, 110, 79, 113, 224, 232, 178, 185, 112, 
                      104, 218, 246, 97, 228, 251, 34, 242, 193, 238, 210, 144, 12, 191, 179, 162, 
                      241, 81, 51, 145, 235, 249, 14, 239, 107, 49, 192, 214, 31, 181, 199, 106, 
                      157, 184, 84, 204, 176, 115, 121, 50, 45, 127, 4, 150, 254, 138, 236, 205, 
                      93, 222, 114, 67, 29, 24, 72, 243, 141, 128, 195, 78, 66, 215, 61, 156, 180]

B = np.reshape(noise,(-1,16))
arr = np.array(B)
print(arr[0][0])
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
for z in range(16):
    for x in range(16):
        block = Block(Vec3(x,round_to_closest(arr[x][z]/100,1),z))
        blocks.append(block)

player = FirstPersonController(jump_duration = 0.25,jump_height = 1,gravity = 1)

app.run()