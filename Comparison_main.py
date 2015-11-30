import os
import pprint
import operator
import pickle
import numpy as np
from training.trainer import *
from training.training_container import *

__author__ = 'touma'


def listdir_fullpath(d):
    return [os.path.join(d, f) for f in os.listdir(d)]


def comparison_main():
    container = TrainingContainer()
    trainer = ImageTrainer(container)

    # Get the vectors from the command line
    # filename = input("Enter filename of training data: ")
    filename = "features_helpme.dat"

    feature_vectors = pickle.load(open(filename, "rb"))


    # This order is fairly important... should keep consistent
    expected_clusters = ['ZoningFeatureExtractor', 'HistogramFeatureExtractor','WeightedVectorsFeatureExtractorX', 'WeightedVectorsFeatureExtractorY']
    #(nickle,dime)
    training_data = []

    files = listdir_fullpath("data/TestValues/Handwritten_half")
    for file in files:
        if file.endswith('png') or file.endswith('jpg') or file.endswith('gif'):
            training_data.append(file)

    fail=[]
    success=0
    total=0
    rejected=0
    skipped = 0
    failed_success=0
    for guess_file in training_data:
        image_vectors = trainer.process_file(guess_file, "DUMMY")

        if image_vectors is None:
            skipped += 1
            continue

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

        if(highest_identified[1]>23):
            rejected+=1
            if(trail[0]=='0' and highest_identified[0]=='zeros'):
                failed_success+=1
            elif(trail[0]=='1' and highest_identified[0]=='ones'):
                failed_success+=1
            elif(trail[0]=='2' and highest_identified[0]=='twos'):
                failed_success+=1
            elif(trail[0]=='3' and highest_identified[0]=='threes'):
                failed_success+=1
            elif(trail[0]=='4' and highest_identified[0]=='fours'):
                failed_success+=1
            elif(trail[0]=='5' and highest_identified[0]=='fives'):
                failed_success+=1
            elif(trail[0]=='6' and highest_identified[0]=='sixs'):
                failed_success+=1
            elif(trail[0]=='7' and highest_identified[0]=='sevens'):
                failed_success+=1
            elif(trail[0]=='8' and highest_identified[0]=='eights'):
                failed_success+=1
            elif(trail[0]=='9' and highest_identified[0]=='nines'):
                failed_success+=1
        else:
            print("File was {} and we identified it as {}".format(guess_file, highest_identified[0]))
            head, trail = os.path.split(guess_file)
            total+=1
            if(trail[0]=='0' and highest_identified[0]=='zeros'):
                success+=1
            elif(trail[0]=='1' and highest_identified[0]=='ones'):
                success+=1
            elif(trail[0]=='2' and highest_identified[0]=='twos'):
                success+=1
            elif(trail[0]=='3' and highest_identified[0]=='threes'):
                success+=1
            elif(trail[0]=='4' and highest_identified[0]=='fours'):
                success+=1
            elif(trail[0]=='5' and highest_identified[0]=='fives'):
                success+=1
            elif(trail[0]=='6' and highest_identified[0]=='sixs'):
                success+=1
            elif(trail[0]=='7' and highest_identified[0]=='sevens'):
                success+=1
            elif(trail[0]=='8' and highest_identified[0]=='eights'):
                success+=1
            elif(trail[0]=='9' and highest_identified[0]=='nines'):
                success+=1
            else:
                fail.append((trail,highest_identified))
            print(highest_identified)

    print("there were {} successes with a percentage of {}".format(success, (success/total)*100))
    print("there were {} rejections".format(rejected))
    print("of the rejections {} would have been identified correctly".format(failed_success))
    print("the following failed")
    for x in fail:
        print(x)
    print("Skipped: {}".format(skipped))
