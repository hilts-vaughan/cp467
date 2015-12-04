__author__ = 'Vaughan Hilts <setsuna> & Brandon Smith'

import math

from PIL import Image

from features.vector_extract_histogram import *
from features.vector_extract_weighted_vectors import *
from thinning.zs_thinner import *
from convolution import *


def filter_test():

    image_to_thin = Image.open('data/thin_test.png').convert('1')
    image_to_thin.show()
    thinner = ZSThinner(image_to_thin)
    thinned_image = thinner.get_thinned_result()

    input("Press enter to continue...")

    thinned_image.show()


    # Apply some convolution filters here
    input("Press enter to continue...")

    sample = Image.open('data/'+input("Enter your picture: (example sample.png)")).convert('I')
    sample.show()

    conv_helper = ConvolutionApplicator()

    input("Press enter to continue...")

    # Iterate over each convolution filter where possible that we support
    for attribute_name in [a for a in dir(ConvolutionApplicator) if not a.startswith('__')]:
        attribute_value = getattr(ConvolutionApplicator, attribute_name)
        if type(attribute_value) is not list:
            continue

        print("Filter: {}".format(attribute_name))

        for x in range(0, len(attribute_value)):
            for y in range(len(attribute_value[0])):
                print("{} ".format(attribute_value[x][y]), end="")
            print("\n")

        image_after = conv_helper.apply(sample, attribute_value)
        image_after.show()
        input("Press enter to continue...")
