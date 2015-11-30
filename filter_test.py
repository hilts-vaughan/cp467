__author__ = 'Vaughan Hilts <setsuna> & Brandon Smith'

import math

from PIL import Image

from features.vector_extract_histogram import *
from features.vector_extract_weighted_vectors import *
from thinning.zs_thinner import *
from convolution import *


def filter_test():

    im = Image.open('data/vector_map.jpg').convert('1')
    image_to_thin = Image.open('data/thin_test.png').convert('1')
    image_to_thin.show()
    thinner = ZSThinner(image_to_thin)
    thinned_image = thinner.get_thinned_result()

    input("press enter to continue")

    pix_array = im.load()

    thinned_image.show()

    # Apply some convolution filters


    input("press enter to continue")

    sample = Image.open('data/sample.png').convert('1')
    sample.show()


    conv_helper = ConvolutionApplicator()
    sample_conv = conv_helper.apply(sample, ConvolutionApplicator.MEDIAN)
    input("press enter to continue")

    sample_conv.show()


    conv_helper = ConvolutionApplicator()
    sample_conv = conv_helper.apply(sample, ConvolutionApplicator.EDGE)
    input("press enter to continue")

    sample_conv.show()

