import numpy as np
from PIL import Image, ImageDraw

print('Enter the background color:')
background_color = str(input())
print('Enter the square color:')
square_color = str(input())
print('Enter the value of k(>0):')
k = int(input())
if k==0:
    print('k should be greater than 0')
    exit(1)


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



img.save('output.png')
