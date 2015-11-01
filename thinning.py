__author__ = 'touma::setsuna'

# Just a statement built-in to fill Git with something
print("Initializing assignment... developers: ", ", ".join(['Vaughan Hilts', 'Brandon Smith'][::-1]))

from PIL import Image

import math
def safe_pixel_getter(pixels,x,y):
    if x<0 or y<0 or x > im.size[0] or y> im.size[1]:
        return 255
    return pixels[x,y]



im = Image.open('test_image_4.png').convert('1')
im2= im.copy()
pix_array=im.load()
pix_array_2=im2.load()
size=im.size
print(size[0])#width so row

strip_pixel=True
even_pass=False

while strip_pixel == True:
    strip_pixel = False
    for k in range(size[0]-1):
            for i in range(size[1]-1):

                con_a = 0
                con_b=False
                con_c=1
                con_d=1
                restore_pixel=0
                for x in range(-1,2):
                    for y in range(-1,2):
                        if(even_pass==True):
                            currentPix = safe_pixel_getter(pix_array, k + x, i + y)
                        else:
                            currentPix = safe_pixel_getter(pix_array_2, k + x, i + y)
                        if(x==0 and y==0):
                                if(currentPix==0):
                                    con_b=True
                                restore_pixel=currentPix
                        if(currentPix==0):
                            con_a += 1#boarder
                        if even_pass==False and( (x==0 and y==-1) or(x==1 and y==0) or (x==0 and y==1)):# p2 p4 p6
                            con_c*=currentPix#condition c first pass
                        elif even_pass==True and( (x==0 and y==-1) or(x==1 and y==0) or (x==-1 and y==0)):#p2 p4 p8
                            con_c*=currentPix#condition c first pass
                        if even_pass==False and( (x==1 and y==0) or (x==0 and y==1) or (x==-1 and y==0)):#p4 p6 p8
                             con_d*=currentPix
                        elif even_pass==True and( (x==0 and y==-1) or(x==0 and y==1) or (x==-1 and y==0)): #p2 p6 p8
                             con_d*=currentPix


                if(con_b==False):
                    if(even_pass==True):
                        pix_array_2[k,i]= restore_pixel
                    else:
                        pix_array[k,i] = restore_pixel
                elif(con_a<=6 and con_a>=2) and con_b==True and con_c==0 and con_d==0:
                    if(even_pass==True):
                        pix_array_2[k,i]=255
                    else:
                        pix_array[k,i] = 255
                    strip_pixel=True
                else:
                    if(even_pass==True):
                        pix_array_2[k,i]=restore_pixel
                    else:
                        pix_array[k,i] = restore_pixel

    even_pass=not even_pass
    if(even_pass==True):
        im2.save("result.png")
    else:
        im.save("result.png")


if(even_pass==True):
    im2.save("result.png")
else:
    im.save("result.png")

