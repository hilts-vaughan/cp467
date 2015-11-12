__author__ = 'Brandon Smith'

# Implements the ZS thinning algorithm in Python
# Provides a very basic pixel locking method for doing so

class ZSThinner:
    BLACK = 0
    WHITE = 255

    def __init__(self, image):
        self.image = image.copy()
        self.pix_array_1 = self.image.load()
        self.size = image.size

    def get_thinned_result(self):
        strip_pixel = True
        even_pass = False

        WHITE = ZSThinner.WHITE
        BLACK = ZSThinner.BLACK
        pix_array_1 = self.pix_array_1

        while strip_pixel:
            strip_pixel = False
            delete = []
            for k in range(self.size[0]-1):
                    for i in range(self.size[1]-1):
                        current=self.safe_pixel_getter(self.pix_array_1, k,i)
                        if(current==BLACK):
                            con_a = 0
                            con_b=0
                            con_c=0
                            con_d=0

                            plist=[current, self.safe_pixel_getter(pix_array_1, k,i-1),self.safe_pixel_getter(pix_array_1, k+1,i-1),self.safe_pixel_getter(pix_array_1, k+1,i),self.safe_pixel_getter(pix_array_1, k+1,i+1),self.safe_pixel_getter(pix_array_1, k,i+1),self.safe_pixel_getter(pix_array_1, k-1,i+1),self.safe_pixel_getter(pix_array_1, k-1,i), self.safe_pixel_getter(pix_array_1, k-1,i-1)]#p1 to p9

                            if even_pass==False and( plist[1]==WHITE or plist[3]==WHITE or plist[5]==WHITE):#c p2=plist[1] p4=plist[3] p6=plist[5]
                                con_c = 1  # condition c first pass

                            elif even_pass==True and( plist[1]==WHITE or plist[3]==WHITE or plist[7]==WHITE):#c' p2 p4 p8 p8=plist[7]
                                con_c = 1  # condition c first pass

                            if even_pass == False and(plist[3]==WHITE or plist[5]==WHITE or plist[7]==WHITE):#d p4 p6 p8
                                con_d = 1

                            elif even_pass == True and( plist[1]==WHITE or plist[5]==WHITE or plist[7]==WHITE): #d' p2 p6 p8
                                con_d = 1

                            for p in range(1,len(plist)-1):
                                if(plist[p]==BLACK):
                                    con_a += 1  # Border

                                if(plist[p+1]==BLACK and plist[p]==WHITE):  # if p+1=black and p is white
                                    con_b += 1

                            if plist[1]==BLACK and plist[8]==WHITE:
                                con_b += 1

                            if(con_a <= 6 and con_a >= 2 ) and con_b == 1 and con_c != 0 and con_d != 0:
                                delete.append([k,i])
                                strip_pixel = True

            even_pass = not even_pass
            for x in delete:
                pix_array_1[x[0],x[1]] = WHITE

        return self.image

    def safe_pixel_getter(self, pixels, x, y):
        if x < 0 or y < 0 or x > self.image.size[0] or y > self.image.size[1]:
            return ZSThinner.WHITE
        return pixels[x, y]
