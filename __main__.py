__author__ = 'touma::setsuna'

# Just a statement built-in to fill Git with something
print("Initializing assignment... developers: ", ", ".join(['Vaughan Hilts', 'Brandon Smith'][::-1]))

from PIL import Image

import math
def sum_of_filters(pixels, filter):
    value=0
    for x in range(len(pixels[0])):
        for y in range(len(filter[0])):
            value+=value+pixels[x][y]*filter[x][y]
    return value

im = Image.open('a_image.tif')
pix_array=im.load()
size=im.size
kernel = [[0, 0, 0], [0,  1, 0],[0, 0, 0]]

fill=Image.new(im.mode,im.size,0)

print(size[0])#width so row

for k in range(size[0]-1):
        for i in range(size[1]-1):

            # Set accumlator
            acc = 0

            try:
                pixels=[
                    [
                        pix_array[k-1,i-1],pix_array[k-1,i],pix_array[k-1,i+1]],[pix_array[k,i-1],pix_array[k,i],pix_array[k,i+1]],[pix_array[k+1,i-1],pix_array[k+1,i],pix_array[k+1,i+1]]
                ]

            # if(k==0):#first row
            #     if(i==0):
            #         pixels=[[0,0,0],[0,pix_array[k,i],pix_array[k,i+1]],[0,pix_array[k+1,i],pix_array[k+1,i+1]]]
            #     elif(i==size[1]):
            #         pixels=[[0,0,0],[pix_array[k,i-1],pix_array[k,i],0],[pix_array[k+1,i+1],pix_array[k+1,i],0]]
            #     else:
            #         pixels=[[0,0,0],[pix_array[k,i-1],pix_array[k,i],pix_array[k,i+1]],[pix_array[k+1,i-1],pix_array[k+1,i],pix_array[k+1,i+1]]]
            # elif(k==size[0]):
            #     if(i==0):
            #         pixels=[[0,pix_array[k-1,i],pix_array[k-1,i+1]],[0,pix_array[k,i],pix_array[k,i+1]],[0,0,0]]
            #     elif(i==size[1]):
            #         pixels=[[pix_array[k-1,i-1],pix_array[k-1,i],0],[pix_array[k,i-1],pix_array[k,i],0],[0,0,0]]
            #     else:
            #         pixels=[[pix_array[k-1,i-1],pix_array[k-1,i],pix_array[k-1,i+1]],[pix_array[k,i-1],pix_array[k,i],pix_array[k,i+1]],[0,0,0]]
            #
            # elif(i==0):
            #      pixels=[[0,pix_array[k-1,i],pix_array[k-1,i+1]],[0,pix_array[k,i],pix_array[k,i+1]],[0,pix_array[k+1,i],pix_array[k+1,i+1]]]
            # elif(i==size[1]):
            #     pixels=[[pix_array[k-1,i-1],pix_array[k-1,i],0],[pix_array[k,i-1],pix_array[k,i],0],[pix_array[k+1,i-1],pix_array[k+1,i],0]]
            # else:
            #     pixels=[[pix_array[k-1,i-1],pix_array[k-1,i],pix_array[k-1,i+1]],[pix_array[k,i-1],pix_array[k,i],pix_array[k,i+1]],[pix_array[k+1,i-1],pix_array[k+1,i],pix_array[k+1,i+1]]]

            print(sum_of_filters(pixels,kernel))
            fill.putpixel([k,i],sum_of_filters(pixels,kernel))

fill.save("testimage.tif")
