__author__ = 'touma::setsuna'

# Just a statement built-in to fill Git with something
print("Initializing assignment... developers: ", ", ".join(['Vaughan Hilts', 'Brandon Smith'][::-1]))

from PIL import Image
from vector_extract import *

import math
def safe_pixel_getter(pixels,x,y):
    if x<0 or y<0 or x > im.size[0] or y> im.size[1]:
        return 0
    return pixels[x,y]

im = Image.open('images.jpg').convert('1')
pix_array=im.load()

# Inori
extractor = FeatureExtractor(im)
vector = extractor.extract_vector(2, 2)
print(vector)

exit()  # Kazusa



size=im.size
#kernel = [[-1, -1, -1,-1,-1], [-1, -1,  15, -1, -1],[-1, -1, -1, -1, -1]]
if(input("press y for edge detection")=="y"):
    kernel=[    [-1 , -1 , -1], [-1, 8, -1], [-1, -1, -1]]
elif(input("press y for box blur")=='y'):
   kernel=[[1/9,1/9,1/9],[1/9,1/9,1/9],[1/9,1/9,1/9]]
elif(input("press y for identity")=='y'):
   kernel=[[0,0,0],[0,1,0],[0,0,0]]
else:
    print("sharpening")
    kernel=[[0 , -1 , 0], [-1, 5, -1], [0, -1, 0]]
print(kernel)
fill=Image.new(im.mode,im.size,0)

print(size[0])#width so row
half_width=math.floor(len(kernel)/2)
half_height=math.floor(len(kernel[0])/2)
print(half_height)
print(half_width)
for k in range(size[0]-1):
        for i in range(size[1]-1):
            acc = 0
            for x in range(-half_width,half_width+1):
                for y in range(-half_height,half_height+1):

                    currentPix = safe_pixel_getter(pix_array, k - x, i - y)
                    kernelPix = kernel[x + half_width][y + half_height]
                    acc += currentPix*kernelPix
            fill.putpixel((k,i),math.floor(acc))




fill.save("testimage2.png")
