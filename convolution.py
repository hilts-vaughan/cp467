import math
from PIL import Image


class ConvolutionApplicator:

    # Provides some default kernels to access for ease
    BOX_BLUR = [[1/9, 1/9, 1/9], [1/9, 1/9, 1/9], [1/9, 1/9, 1/9]]
    #IDENTITY = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    SHARPEN = [[0, -1, 0], [-1, 5, -1], [0, -1, 0]]
    EDGE = [[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]]
    MEDIAN = [[6, 2, 0], [3, 97, 4], [19, 3, 10]]  # http://www.markschulze.net/java/meanmed.html
    EMBOSS = [[-2, -1, 0], [-1, 1, 1], [0, 1, 2]]
    EMPHASIS_BOTTOM = [[1, 1, 1], [1, 1, 1], [-1, -1, -1]]
    TOP_SOBEL = [[1, 2, 1], [0, 0, 0], [-1, -2, -1]]
    RIGHT_SOBEL = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
    FIVE_GUASSIAN = [[1/273, 4/273, 7/237, 4/237, 1/237], [4/237, 16/237, 26/237, 16/237, 4/237], [7/237, 26/237, 41/237, 26/237, 7/237], [4/237, 16/237, 26/237, 16/237, 4/237], [1/237, 4/237, 7/237, 4/237, 1/237]]

    def __init__(self):
        return

    def safe_pixel_getter(self, pixels, x , y, size):
        if x < 0 or y < 0 or x > size[0] - 1 or y > size[1] - 1:
            return 0
        return pixels[x, y]

    # Applies a kernel to the image, a copy is made inside of the applicator so it's read-only
    def apply(self, image, kernel):
        workingImage = image.copy()
        pix_array = workingImage.load()

        half_width = math.floor(len(kernel)/2)
        half_height = math.floor(len(kernel[0])/2)
        fill = Image.new('1', workingImage.size)
        size = fill.size

        for k in range(size[0]-1):
                for i in range(size[1]-1):
                    acc = 0
                    for x in range(-half_width,half_width+1):
                        for y in range(-half_height,half_height+1):
                            currentPix = self.safe_pixel_getter(pix_array, k - x, i - y, size)
                            kernelPix = kernel[x + half_width][y + half_height]
                            acc += currentPix*kernelPix
                    fill.putpixel((k, i), math.floor(acc))
        return fill



