__author__ = 'Vaughan Hilts <setsuna> & Brandon Smith'

import math

from PIL import Image

from features.vector_extract_histogram import *
from features.vector_extract_weighted_vectors import *
from thinning.zs_thinner import *
from convolution import *

im = Image.open('data/vector_map.jpg').convert('1')
image_to_thin = Image.open('data/thin_test.png').convert('1')
sample = Image.open('data/sample.png').convert('1')

pix_array = im.load()

# Inori
extractor = HistogramFeatureExtractor(im)
extractor2 = WeightedVectorsFeatureExtractor(im)

vector = extractor.extract_vector(2, 2)
vector2 = extractor2.extract_vector(2, 2)
print(vector)
print(vector2)

thinner = ZSThinner(image_to_thin)
thinned_image = thinner.get_thinned_result()
thinned_image.save("results/thinned.png")

# Apply some convolution filters
conv_helper = ConvolutionApplicator()
sample_conv = conv_helper.apply(sample, ConvolutionApplicator.MEDIAN)
sample_conv.save('results/convolution.png')
sample_conv.show()

