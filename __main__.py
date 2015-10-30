__author__ = 'touma::setsuna'

# Just a statement built-in to fill Git with something
print("Initializing assignment... developers: ", ", ".join(['Vaughan Hilts', 'Brandon Smith'][::-1]))

from PIL import Image

import math
def safe_pixel_getter(pixels,x,y):

    if x<0 or y<0 or x > im.size[0] or y> im.size[1]:
        return 0
    return pixels[x,y]



im = Image.open('download_again.jpg').convert('L')
pix_array=im.load()
size=im.size
kernel = [[-1, -1, -1,-1,-1], [-1, -1,  15, -1, -1],[-1, -1, -1, -1, -1]]
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
            for x in range(-half_width,half_width):
                for y in range(-half_height,half_height):
                    currentPix = safe_pixel_getter(pix_array, k + x, i + y)

                    kernelPix = kernel[x + half_width][y + half_height]
                    acc += currentPix*kernelPix
            fill.putpixel((k,i),math.floor(acc))

                    # pixels[len(kernel)-x,len(kernel[0])-y]=pix_array[safe_pixel_getter(pix_array, k-x, i-y)] #get the current pixel array. pix_array is not an array of pixels does not have a len function

            # Set accumlator
            # pixels=[[pix_array[k-1,i-1],pix_array[k-1,i],pix_array[k-1,i+1]],[pix_array[k,i-1],pix_array[k,i],pix_array[k,i+1]],[pix_array[k+1,i-1],pix_array[k+1,i],pix_array[k+1,i+1]]]



fill.save("testimage2.png")
