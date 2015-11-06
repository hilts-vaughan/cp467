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
pix_array_1=im1.load()
size=im1.size
print(size[0])#width so row

strip_pixel=True
even_pass=False

start_time = time.time()

while strip_pixel == True:
    strip_pixel = False
    delete=[]
    for k in range(size[0]-1):
            for i in range(size[1]-1):
                current=safe_pixel_getter(pix_array_1, k,i)
                if(current==BLACK):
                    con_a = 0
                    con_b=0
                    con_c=0
                    con_d=0

                    plist=[current, safe_pixel_getter(pix_array_1, k,i-1),safe_pixel_getter(pix_array_1, k+1,i-1),safe_pixel_getter(pix_array_1, k+1,i),safe_pixel_getter(pix_array_1, k+1,i+1),safe_pixel_getter(pix_array_1, k,i+1),safe_pixel_getter(pix_array_1, k-1,i+1),safe_pixel_getter(pix_array_1, k-1,i), safe_pixel_getter(pix_array_1, k-1,i-1)]#p1 to p9

                    if even_pass==False and( plist[1]==WHITE or plist[3]==WHITE or plist[5]==WHITE):#c p2=plist[1] p4=plist[3] p6=plist[5]
                         con_c=1#condition c first pass

                    elif even_pass==True and( plist[1]==WHITE or plist[3]==WHITE or plist[7]==WHITE):#c' p2 p4 p8 p8=plist[7]
                        con_c=1#condition c first pass

                    if even_pass==False and(plist[3]==WHITE or plist[5]==WHITE or plist[7]==WHITE):#d p4 p6 p8
                        con_d=1

                    elif even_pass==True and( plist[1]==WHITE or plist[5]==WHITE or plist[7]==WHITE): #d' p2 p6 p8
                        con_d=1

                    #con B is weird...
                    for p in range(1,len(plist)-1):
                        if(plist[p]==BLACK):
                            con_a +=1#boarder

                        if(plist[p+1]==BLACK and plist[p]==WHITE): #if p+1=black and p is white
                            con_b+=1

                    if plist[1]==BLACK and plist[8]==WHITE:
                        con_b+=1

                    if(con_a<=6 and con_a>=2) and con_b==1 and con_c!=0 and con_d!=0:
                        delete.append([k,i])
                        strip_pixel=True


    print("--- %s seconds ---" % (time.time() - start_time))
    even_pass=not even_pass
    for x in delete:
        pix_array_1[x[0],x[1]]=WHITE
    #the following is just so i can see changes as the program runs
    #if(even_pass==True):
     #   im2.save("result.png")
    #else:
     #   im1.save("result.png")
im1.save("result.png")

