__author__ = 'touma::setsuna'

# Just a statement built-in to fill Git with something
print("Initializing assignment... developers: ", ", ".join(['Vaughan Hilts', 'Brandon Smith'][::-1]))

from PIL import Image
import time
import math
def safe_pixel_getter(pixels,x,y):
    if x<0 or y<0 or x > im1.size[0] or y> im1.size[1]:
        return WHITE
    return pixels[x,y]


BLACK=0
WHITE=255
im1 = Image.open('test_image_4.png').convert('1')
im2= im1.copy()
pix_array_1=im1.load()
pix_array_2=im2.load()
size=im1.size
print(size[0])#width so row

strip_pixel_odd=True
strip_pixel_even=True
even_pass=False

start_time = time.time()

while strip_pixel_odd == True or strip_pixel_even==True:
    if(even_pass==True):
        strip_pixel_odd = False
    else:
        strip_pixel_even = False
    for k in range(size[0]-1):
            for i in range(size[1]-1):
                con_a = 0
                con_b=0
                con_c=0
                con_d=0
                for x in range(-1,2):#-1 to 1 inclusive
                    for y in range(-1,2):
                        if(even_pass==True):
                            plist=[safe_pixel_getter(pix_array_1, k,i), safe_pixel_getter(pix_array_1, k,i-1),safe_pixel_getter(pix_array_1, k+1,i-1),safe_pixel_getter(pix_array_1, k+1,i),safe_pixel_getter(pix_array_1, k+1,i+1),safe_pixel_getter(pix_array_1, k,i+1),safe_pixel_getter(pix_array_1, k-1,i+1),safe_pixel_getter(pix_array_1, k-1,i), safe_pixel_getter(pix_array_1, k-1,i-1)]#p2 to p9
                        else:
                            plist=[safe_pixel_getter(pix_array_2, k,i-1),safe_pixel_getter(pix_array_2, k,i-1),safe_pixel_getter(pix_array_2, k+1,i-1),safe_pixel_getter(pix_array_2, k+1,i),safe_pixel_getter(pix_array_2, k+1,i+1),safe_pixel_getter(pix_array_2, k,i+1),safe_pixel_getter(pix_array_2, k-1,i+1),safe_pixel_getter(pix_array_2, k-1,i), safe_pixel_getter(pix_array_2, k-1,i-1)]

                        if(even_pass==True):
                            currentPix = safe_pixel_getter(pix_array_1, k + x, i + y)#grab from where we currently are
                        else:
                            currentPix = safe_pixel_getter(pix_array_2, k + x, i + y)
                        if(currentPix==BLACK and x!=0 and y!=0):#neighbours that are black
                            con_a += 1#boarder
                        #c
                        if even_pass==False and( (x==0 and y==-1) or(x==1 and y==0) or (x==0 and y==1)):# p2 p4 p6
                            con_c+=currentPix#condition c first pass
                        #c'
                        elif even_pass==True and( (x==0 and y==-1) or(x==1 and y==0) or (x==-1 and y==0)):#p2 p4 p8
                            con_c+=currentPix#condition c first pass
                        #d
                        if even_pass==False and( (x==1 and y==0) or (x==0 and y==1) or (x==-1 and y==0)):#p4 p6 p8
                             con_d+=currentPix
                        #d'
                        elif even_pass==True and( (x==0 and y==-1) or(x==0 and y==1) or (x==-1 and y==0)): #p2 p6 p8
                             con_d+=currentPix

                #con B is weird...
                if(even_pass==True):
                    plist=[safe_pixel_getter(pix_array_1, k,i-1),safe_pixel_getter(pix_array_1, k+1,i-1),safe_pixel_getter(pix_array_1, k+1,i),safe_pixel_getter(pix_array_1, k+1,i+1),safe_pixel_getter(pix_array_1, k,i+1),safe_pixel_getter(pix_array_1, k-1,i+1),safe_pixel_getter(pix_array_1, k-1,i), safe_pixel_getter(pix_array_1, k-1,i-1)]#p2 to p9
                else:
                    plist=[safe_pixel_getter(pix_array_2, k,i-1),safe_pixel_getter(pix_array_2, k+1,i-1),safe_pixel_getter(pix_array_2, k+1,i),safe_pixel_getter(pix_array_2, k+1,i+1),safe_pixel_getter(pix_array_2, k,i+1),safe_pixel_getter(pix_array_2, k-1,i+1),safe_pixel_getter(pix_array_2, k-1,i), safe_pixel_getter(pix_array_2, k-1,i-1)]
                for p in range(0,len(plist)-1):
                    if(plist[p+1]==BLACK and plist[p]==WHITE): #if p+1=black and p is white
                        con_b+=1

                if plist[0]==BLACK and plist[7]==WHITE:
                    con_b+=1

                if(con_a<=6 and con_a>=2) and con_b==1 and con_c!=0 and con_d!=0 and pix_array_1[k,i]==BLACK:
                    if(even_pass==True):
                        pix_array_2[k,i]=WHITE
                        strip_pixel_even=True
                    elif(even_pass==False):
                        pix_array_1[k,i] = WHITE
                        strip_pixel_odd=True
                    #else no changes between two images should not require an overwrite
                else:
                    if even_pass==True:
                        pix_array_2[k,i]=pix_array_1[k,i]
                    else:
                        pix_array_1[k,i]=pix_array_2[k,i]
    print("--- %s seconds ---" % (time.time() - start_time))
    even_pass=not even_pass
    #the following is just so i can see changes as the program runs
    #if(even_pass==True):
     #   im2.save("result.png")
    #else:
     #   im1.save("result.png")
if(even_pass==True):
    im2.save("result.png")
else:
    im1.save("result.png")

1