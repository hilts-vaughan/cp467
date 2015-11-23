import os
import pprint
import operator
import pickle
import numpy as np
from training.trainer import *
from training.training_container import *

__author__ = 'touma'

container = TrainingContainer()
trainer = ImageTrainer(container)

# Get the vectors from the command line
# filename = input("Enter filename of training data: ")
filename = "features.dat"

feature_vectors = pickle.load(open(filename, "rb"))


# This order is fairly important... should keep consistent
expected_clusters = ['HistogramFeatureExtractor', 'WeightedVectorsFeatureExtractorX', 'WeightedVectorsFeatureExtractorY', 'ZoningFeatureExtractor']

training_data = ["mono/8.png"]

for guess_file in training_data:
    image_vectors = trainer.process_file(os.path.join(os.getcwd(), "data/training/", guess_file), "DUMMY")

    deltas = {}

    for key, value in feature_vectors.items():
        deltas[key] = []
        for cluster in expected_clusters:
            # print(cluster + ", " + key)
            # print(image_vectors[cluster])
            # print(value[cluster])

            # Subtract the two
            delta_list = list(map(operator.sub, image_vectors[cluster], value[cluster]))
            delta = np.linalg.norm(np.array(delta_list))
            # print(delta)
            deltas[key].append(delta)
        print(key)
        print(deltas[key])

    # Identify given the deltas the winners...
    print("Judging... please be patient")
    highest_identified = ('', 9999)
    for key, value in deltas.items():
        delta = np.linalg.norm(np.array(value))
        if delta < highest_identified[1]:
            highest_identified = (key, delta)

    print("File was {} and we identified it as {}".format(guess_file, highest_identified[0]))
