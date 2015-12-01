import os
import pprint
import operator
import pickle
import numpy as np
from scipy import stats
from training.trainer import *
from training.training_container import *

__author__ = 'touma'


def listdir_fullpath(d):
    return [os.path.join(d, f) for f in os.listdir(d)]


def comparison_main():
    container = TrainingContainer()
    trainer = ImageTrainer(container)

    # Get the vectors from the command line
    filename = input("Enter filename of training data: ")
    # filename = "disc.dat"

    feature_vectors = pickle.load(open(filename, "rb"))


    # This order is fairly important... should keep consistent
    expected_clusters = ['ZoningFeatureExtractor', 'HistogramFeatureExtractor', 'WeightedVectorsFeatureExtractorX',  'WeightedVectorsFeatureExtractorY', 'BottomDiscriminationFeatureExtractor']
    training_data = []

    files = listdir_fullpath("data/TestValues/Handwritten")
    for file in files:
        if file.endswith('png') or file.endswith('jpg') or file.endswith('gif'):
            training_data.append(file)

    fail= []
    success = 0

    # Used for keeping track of successes
    success_table = {}
    rejection_table = {}

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
                delta = np.linalg.norm(np.array(delta_list), 1)
                # print(delta)
                deltas[key].append(delta)
            # print(key)
            # print(deltas[key])

        # Identify given the deltas the winners...
        highest_identified = ('', 9999)
        for key, value in deltas.items():
            delta = np.linalg.norm(np.array(value))
            if delta < highest_identified[1]:
                highest_identified = (key, delta)

        if(highest_identified[1]>11.8):
            rejected+=1
            head, trail = os.path.split(guess_file)

            # Record old value for comparison
            old_failed_success = failed_success

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
            print("File was {} and we identified it as {} with delta {}".format(guess_file, highest_identified[0], highest_identified[1]))
            head, trail = os.path.split(guess_file)
            total+=1
            old_success = success
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
                fail.append((trail, highest_identified))

            # There was an update, append to the table
            if success > old_success:
                if highest_identified[0] not in success_table:
                    success_table[highest_identified[0]] = []
                success_table[highest_identified[0]].append(highest_identified[1])
            else:
                # We rejected incorrectly; record the delta for this
                # so we can learn from our mistakes
                if trail[0] not in rejection_table:
                    rejection_table[trail[0]] = []
                rejection_table[trail[0]].append(highest_identified[1])

    print("There were {} successes with a percentage of {}".format(success, (success/total)*100))

    print("{:<8} {:<15} {:<10}".format('Symbol', 'Correct (%)', 'Incorrect (%)'))
    for k, v in success_table.items():
        count = len(v)
        correct = (count / 100) * 100
        print("{:<8} {:<15} {:<10}".format(k, correct, 100 - correct))

    print("There were {} rejections made.".format(rejected))
    print("Of the rejections made, {} would have been identified correctly. ".format(failed_success))

    print("{:<8} {:<15} {:<5}".format('Symbol', 'Trimmed Mean', 'Standard Deviation'))
    for k, v in rejection_table.items():
        correct = stats.trim_mean(v, 0.05)
        std = np.std(v)
        print("{:<8} {:<15} {:<5}".format(k, correct, std))

    # print("The following failed: ")
    # for x in fail:
    #     print(x)

    print("Skipped: {}".format(skipped))
