__author__ = 'Vaughan Hilts <setsuna>'

# Extracts a feature vector from a given chunk mechanism.
# Allows extracting from images, simply over-riding the
# accumlator function to implement your logic for the vector
# ratios.

# This particular implementation offers the ability to count weighted
# bearings in a particular section based on the origin point. These are
# later used with training data to form the weight vectors.


class WeightedVectorsFeatureExtractor:

    def __init__(self, image):
        self.image = image
        self.imageData = image.load()

    # Given an image and number of chunks in both axis, gives the
    # vector back containins chunksWide * chunksHigh elements
    def extract_vector(self, chunksWide, chunksHigh):
        vector = []

        for y in range(0, chunksWide):
            for x in range(0, chunksHigh):
                bounds = self.__get_chunk_bound(chunksWide, chunksHigh, x, y)
                # Compute vector for bounds
                vector.append(self.__get_value_for_bound(bounds))

        a, b = zip(*vector)
        return list(a), list(b)

    def __get_chunk_bound(self, chunksWide, chunksHigh, x, y):
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

    def __get_value_for_bound(self, bounds):
        lower = bounds[0]
        upper = bounds[1]

        accX = 0
        accY = 0
        total = 0

        # Get the vector value
        for y in range(lower[1], upper[1]):
            for x in range(lower[0], upper[0]):
                if self.imageData[x, y] == 0:
                    accX = accX + x - lower[0]
                    accY = accY + y - lower[1]
                    total += 1

        if total is 0:
            total = 1

        # Chebyshev Distance
        return ( accX / total) / (upper[0] - lower[0]), (accY / total) / (upper[1] - lower[1])
