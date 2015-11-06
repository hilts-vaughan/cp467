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
                delete=[]
                if(even_pass==True):
                    plist=[safe_pixel_getter(pix_array_1, k,i), safe_pixel_getter(pix_array_1, k,i-1),safe_pixel_getter(pix_array_1, k+1,i-1),safe_pixel_getter(pix_array_1, k+1,i),safe_pixel_getter(pix_array_1, k+1,i+1),safe_pixel_getter(pix_array_1, k,i+1),safe_pixel_getter(pix_array_1, k-1,i+1),safe_pixel_getter(pix_array_1, k-1,i), safe_pixel_getter(pix_array_1, k-1,i-1)]#p2 to p9
                else:
                    plist=[safe_pixel_getter(pix_array_2, k,i-1),safe_pixel_getter(pix_array_2, k,i-1),safe_pixel_getter(pix_array_2, k+1,i-1),safe_pixel_getter(pix_array_2, k+1,i),safe_pixel_getter(pix_array_2, k+1,i+1),safe_pixel_getter(pix_array_2, k,i+1),safe_pixel_getter(pix_array_2, k-1,i+1),safe_pixel_getter(pix_array_2, k-1,i), safe_pixel_getter(pix_array_2, k-1,i-1)]

                if even_pass==False and( plist[1]==WHITE or plist[3]==WHITE or plist[5]):#c p2=plist[1] p4=plist[3] p6=plist[5]
                     con_c+=1#condition c first pass

                elif even_pass==True and( plist[1]==WHITE or plist[3]==WHITE or plist[7]):#c' p2 p4 p8 p8=plist[7]
                    con_c+=1#condition c first pass

                if even_pass==False and(plist[3]==WHITE or plist[5]==WHITE or plist[7]):#d p4 p6 p8
                    con_d+=1

                elif even_pass==True and( plist[1]==WHITE or plist[5]==WHITE or plist[7]): #d' p2 p6 p8
                    con_d+=1

                #con B is weird...
                for p in range(1,len(plist)-1):
                    if(plist[p]==BLACK):
                        con_a +=1#boarder

                    if(plist[p+1]==BLACK and plist[p]==WHITE): #if p+1=black and p is white
                        con_b+=1

                if plist[1]==BLACK and plist[8]==WHITE:
                    con_b+=1

                if(con_a<=6 and con_a>=2) and con_b==1 and con_c!=0 and con_d!=0 and pix_array_1[k,i]==BLACK:
                    delete.append([k,i])
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

