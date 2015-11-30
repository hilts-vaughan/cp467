__author__ = 'Vaughan Hilts <setsuna> & Brandon Smith'

import math

from PIL import Image

from features.vector_extract_histogram import *
from features.vector_extract_weighted_vectors import *
from thinning.zs_thinner import *
from convolution import *


def filter_test():

    #im = Image.open('data/vector_map.jpg').convert('1')
    image_to_thin = Image.open('data/thin_test.png').convert('1')
    image_to_thin.show()
    thinner = ZSThinner(image_to_thin)
    thinned_image = thinner.get_thinned_result()

    input("press enter to continue")

    #pix_array = im.load()

    thinned_image.show()

    # Apply some convolution filters


    input("press enter to continue")

    sample = Image.open('data/'+input("enter your picture (example sample.png)")).convert('1')
    sample.show()


    #conv_helper = ConvolutionApplicator()
    #sample_conv = conv_helper.apply(sample, ConvolutionApplicator.MEDIAN)
    #print("median filter")
    #filter_example=[[6, 2, 0], [3, 97, 4], [19, 3, 10]]  # http://www.markschulze.net/java/meanmed.html
    #for x in filter_example:
    #    print(x)
    #input("press enter to continue")

    #sample_conv.show()


    conv_helper = ConvolutionApplicator()
    sample_conv = conv_helper.apply(sample, ConvolutionApplicator.EDGE)
    print("high pass edge detection")
    filter_example=[[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]]  # http://www.markschulze.net/java/meanmed.html
    for x in filter_example:
        print(x)
    input("press enter to continue")
    sample_conv.show()

    conv_helper = ConvolutionApplicator()
    sample_conv = conv_helper.apply(sample, ConvolutionApplicator.BOX_BLUR)

    print("low pass box blur")
    filter_example=[[1/9, 1/9, 1/9], [1/9, 1/9, 1/9], [1/9, 1/9, 1/9]]  # http://www.markschulze.net/java/meanmed.html
    for x in filter_example:
        print(x)
    input("press enter to continue")
    sample_conv.show()
