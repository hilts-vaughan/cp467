from math import *

__author__ = 'vaughanhilts'


# Extracts a feature vector from a given chunk mechanism.
# Allows extracting from images, simply over-riding the
# accumlator function to implement your logic for the vector
# ratios
class FeatureExtractor:

    def __init__(self, image):
        self.image = image
        self.imageData = image.load()

    # Given an image and number of chunks in both axis, gives the
    # vector back containins chunksWide * chunksHigh elements
    def extract_vector(self, chunksWide, chunksHigh):
        vector = []

        for y in range(0, chunksWide):
            for x in range(0, chunksHigh):
                bounds = self._get_chunk_bound(chunksWide, chunksHigh, x, y)
                # Compute vector for bounds
                vector.append(self._get_value_for_bound(bounds))
        return vector

    def _get_chunk_bound(self, chunksWide, chunksHigh, x, y):
        size = self.image.size
        imageWidth = size[0]
        imageHeight = size[1]

        blockWidth =  imageWidth // chunksWide
        blockHeight = imageHeight // chunksHigh

        lowerX = blockWidth * x
        lowerY = blockHeight * y

        highX = min(imageWidth, blockWidth * (x + 1))
        highY = min(imageHeight, blockHeight * (y + 1))

        return [(lowerX, lowerY), (highX, highY)]  # Returns the empty bound

    def _get_value_for_bound(self, bounds):
        lower = bounds[0]
        upper = bounds[1]
        acc = 0
        total = 0

        # Get the vector value
        for y in range(lower[1], upper[1]):
            for x in range(lower[0], upper[0]):
                if self.imageData[x, y] == 0:
                    acc = acc + 1
                total = total + 1
        return acc / total
