import os
from convolution import *
from PIL import Image, ImageChops, ImageOps
from training.training_container import *
from features.vector_extract_histogram import *
from features.vector_extract_weighted_vectors import *

# This class should be able to take a series of images and then extract features about them, and stick them into
# clusters for viewing later. The program is manually supervised.

__author__ = 'touma'


class Comparison:

    def __init__(self):
        self.cluster = 0
        return

    def listdir_fullpath(self, d):
        return [os.path.join(d, f) for f in os.listdir(d)]

    def train_directory(self, img_dir, training_dir ):
        files = self.listdir_fullpath(img_dir)
        for file in files:
            if file.endswith('png') or file.endswith('jpg') or file.endswith('gif'):
                self.process_file(file,training_dir)

    def process_file(self, file):
        print("Processing: {}".format(file))
        # We only want 1 bit images; this should help peel some noise away
        image = Image.open(file).convert('1')
        image = self.pre_process_image(image)
        self.cluster = self.compute_vector_cluster(image)

    def trim(self, im):
        w, h = im.size
        invert_im = im.convert("RGB")
        invert_im = ImageOps.invert(invert_im)
        invert_im = invert_im.crop((0, 2, w - 2, h - 2))
        bbox = invert_im.getbbox()
        if bbox:
            return im.crop(bbox)

    # Do any pre-processing on the image here that may be needed; thin, median etc.
    def pre_process_image(self, image):
        helper = ConvolutionApplicator()
        image = helper.apply(image, ConvolutionApplicator.MEDIAN)
        image = self.trim(image)
        return image

    def compute_vector_cluster(self, image):
        #extractors = [HistogramFeatureExtractor, WeightedVectorsFeatureExtractor]
        extractors=[HistogramFeatureExtractor]
        #block_size = 2 vaughans values
        block_size=4
        cluster = TrainingCluster()

        for extractor in extractors:
            instance = extractor(image)
            vector = instance.extract_vector(block_size, block_size)

            # Add to the cluster
            cluster.add_vector(extractor.__name__, vector)
        return cluster


