import cv2
from math import sin,cos

def lerp(a0,a1,w):
    return float((a1-a0) * w + a0)

def random_gradient(ix, iy):
    ix = int(ix)
    iy = int(iy)
    random = 2920.0 * sin(ix * 21942.0 + iy * 171324.0 + 8912.0) * cos(ix * 23157.0 * iy * 217832.0 + 9758.0)
    return (cos(random),sin(random))

def dot_grid_gradient(ix, iy, x, y):
    ix = float(ix)
    iy = float(iy)
    x = float(x)
    y = float(y)

    gradient = random_gradient(ix,iy)

    dx = float(x - float(ix))
    dy = float(y - float(iy))

    return (float(dx * gradient[0]) + float(dy * gradient[1]))

def gen_perlin_noise(x,y):
    x0 = int(x)
    x1 = x0 + 1 
    y0 = int(y)
    y1 = y0 + 1

    sx = float(x) - float(x0)
    sy = float(y) - float(y0)

    n0 = dot_grid_gradient(x0,y0,x,y)
    n1 = dot_grid_gradient(x1,y0,x,y)
    ix0 = lerp(n0,n1,sx)

    n0 = dot_grid_gradient(x0,y1,x,y)
    n1 = dot_grid_gradient(x1,y1,x,y)
    ix1 = lerp(n0,n1,sx)

    value = lerp(float(ix0),float(ix1),float(sy))
    return value

final = []
for y in range(100):
    row = []
    for x in range(100):
        row.append(gen_perlin_noise(float(x),float(y)))
    final.append(row)

print(final)