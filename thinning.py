__author__ = 'touma::setsuna'

# Just a statement built-in to fill Git with something
print("Initializing assignment... developers: ", ", ".join(['Vaughan Hilts', 'Brandon Smith'][::-1]))

from PIL import Image

import math
def safe_pixel_getter(pixels,x,y):

    if x<0 or y<0 or x > im.size[0] or y> im.size[1]:
        return 0
    return pixels[x,y]



im = Image.open('image_test.png').convert('1')
pix_array=im.load()
size=im.size
fill=im.copy()
fill.save("test_image3.png")
print(size[0])#width so row

strip_pixel=True
even_pass=False

while strip_pixel == True:
    im = Image.open("test_image3.png")
    pix_array=im.load()
    size=im.size
    fill=Image.new(im.mode,im.size,0)

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
                        currentPix = safe_pixel_getter(pix_array, k + x, i + y)
                        if(currentPix>0):
                            con_a += 1#boarder
                            if(x==0 and y==0):
                                con_b=True
                                restore_pixel=currentPix

                        if even_pass==False and( (x==0 and y==-1) or(x==1 and y==0) or (x==0 and y==1)):# p2 p4 p6
                            con_c*=currentPix#condition c first pass
                        elif even_pass==True and( (x==0 and y==-1) or(x==1 and y==0) or (x==-1 and y==0)):#p2 p4 p8
                            con_c*=currentPix#condition c first pass
                        if even_pass==False and( (x==1 and y==0) or (x==0 and y==1) or (x==-1 and y==0)):#p4 p6 p8
                             con_d*=currentPix
                        elif even_pass==True and( (x==0 and y==-1) or(x==0 and y==1) or (x==-1 and y==0)): #p2 p6 p8
                             con_d*=currentPix
                if(con_b==False):
                    fill.putpixel((k,i),0)
                elif(con_a<=6 and con_a>=2) and con_b==True and con_c==0 and con_d==0:
                    fill.putpixel((k,i),255)
                    strip_pixel=True
                else:
                    fill.putpixel((k,i),0)

    even_pass=not even_pass
    fill.save("test_image3.png")

