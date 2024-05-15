import numpy as np
from PIL import Image, ImageDraw


background_color = str(input())
square_color = str(input())
k = int(input())


img = Image.new('RGB', (3**k, 3**k), background_color)
dib = ImageDraw.Draw(img)

def get_coord(k):
    coord = np.empty((0,2))
    for j in range(3**(k-1)):
        for i in range(3**(k-1)):
            val = np.array([[1.5 + 3 * i, 1.5 + 3 * j]])
            coord = np.append(coord, val, axis = 0)
    return coord


for i in range(k):
    for j in range(9**i):
        dib.regular_polygon((get_coord(i+1)[j]*3**(k-(i+1)), 0.5*3**(k-(i+1))),4, fill=square_color)


# dib.regular_polygon((1.5, 1.5, 0.5), 4, fill=square_color)

# dib.regular_polygon((coord[j]*3**(k-(i+1)), 3**(k-1-i)/np.sqrt(2)),4, fill=square_color)

img.save('output.png')
