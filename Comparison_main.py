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

training_data = ["01.png", "11.png","21.png","31.png","41.png","51.png","61.png","71.png","81.png","91.png","02.png", "12.png","22.png","32.png","42.png","52.png","62.png","72.png","82.png","92.png"]

fail=[]
success=0
for guess_file in training_data:
    image_vectors = trainer.process_file(os.path.join(os.getcwd(), "data/TestValues/", guess_file), "DUMMY")

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
    if(guess_file[0]=='0' and highest_identified[0]=='zeros'):
        success+=1
    elif(guess_file[0]=='1' and highest_identified[0]=='ones'):
        success+=1
    elif(guess_file[0]=='2' and highest_identified[0]=='twos'):
        success+=1
    elif(guess_file[0]=='3' and highest_identified[0]=='threes'):
        success+=1
    elif(guess_file[0]=='4' and highest_identified[0]=='fours'):
        success+=1
    elif(guess_file[0]=='5' and highest_identified[0]=='fives'):
        success+=1
    elif(guess_file[0]=='6' and highest_identified[0]=='sixs'):
        success+=1
    elif(guess_file[0]=='7' and highest_identified[0]=='sevens'):
        success+=1
    elif(guess_file[0]=='8' and highest_identified[0]=='eights'):
        success+=1
    elif(guess_file[0]=='9' and highest_identified[0]=='nines'):
        success+=1
    else:
        fail.append((guess_file,highest_identified))


print("there were {} successes".format(success))
print("the following failed")
for x in fail:
    print(x)
