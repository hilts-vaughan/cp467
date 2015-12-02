import os
import pprint
import operator
import pickle
import numpy as np
import matplotlib.pyplot as plt

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

    feature_vectors = pickle.load(open(filename, "rb"))

    needs_filtering = False
    rejections_allowed = False

    if input("Do you need filtering for this run? (y/n)") is 'y':
        needs_filtering = True

    if input("Enable rejections for this run? (y/n)") is 'y':
        rejections_allowed = True

    compare_path = input("What sample set to run against? ")

    # This order is fairly important... should keep consistent
    expected_clusters = ['ZoningFeatureExtractor', 'HistogramFeatureExtractor', 'WeightedVectorsFeatureExtractorX',  'WeightedVectorsFeatureExtractorY', 'BottomDiscriminationFeatureExtractor']
    training_data = []

    files = listdir_fullpath("data/TestValues/{}".format(compare_path))
    for file in files:
        if file.endswith('png') or file.endswith('jpg') or file.endswith('gif'):
            training_data.append(file)

    fail= []
    success = 0

    # Used for keeping track of successes
    success_table = {}

    attempt_table = {}
    attempt_lookup = ['zeros', 'ones', 'twos', 'threes', 'fours', 'fives', 'sixs', 'sevens', 'eights', 'nines']

    # Computed from runs of good data; see Appendix
    # If you want "higher confidence" multiply the last number by two
    # One deviation = 65% confident, 2 = 95% confident (higher = more mistakes let through)
    # Linearly mapped for those that are not Z-score < 3 (linearly interpolated up)
    rejection_table = {
        'ones': 1.08699955735919 + 0.3557285581468123*2.4,
        'sevens': 0.3791196943169978 + 0.15244101203498067*6.5,
        'fours': 0.5670250474976859 + 0.20740505076486368*3.5,
        'zeros': 0.4637782896543876 + 0.11720196366413335*6.5,
        'fives': 0.765784657657991 + 0.16640374063038987*3,
        'twos': 0.6239159354846676 + 0.12782956438988816*1.45,
        'threes': 0.657972456689225 + 0.15544727545884507*3.7,
        'nines': 0.6202502632483777 + 0.2767916192461189*2.7,
        'sixs': 0.54491864105959 + 0.16740085588129852*3.6,
        'eights': 0.5262590927801994 + 0.11219700395006942*3.5
    }

    total=0
    rejected=0
    skipped = 0
    failed_success=0
    for guess_file in training_data:
        image_vectors = trainer.process_file(guess_file, "DUMMY", needs_filtering)

        if image_vectors is None:
            skipped += 1
            continue

        deltas = {}

        for key, value in feature_vectors.items():
            deltas[key] = []

            if key not in success_table:
                success_table[key] = []
                attempt_table[key] = 0

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

        if rejections_allowed and highest_identified[1] > rejection_table[highest_identified[0]]:
            rejected += 1
            head, trail = os.path.split(guess_file)

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

            # We didn't reject, so record an attempt
            if trail[0].isnumeric():
                attempt_table[attempt_lookup[int(trail[0])]] += 1

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
                success_table[highest_identified[0]].append(highest_identified[1])

    print("There were {} successes (out of {} guesses) for a percentage of {}".
          format(success, sum(attempt_table.values()), (success/total)*100))
    print("{:<8} {:<15} {:<10} {:<15} {:<15}".format('Symbol', 'Correct (%)', 'Incorrect (%)', 'Average Delta', 'Std. Delta'))
    for k, v in success_table.items():
        count = len(v)

        correct = 0.0
        mu = float("inf")
        std = float("inf")

        if attempt_table[k] > 0:
            correct = (count / attempt_table[k]) * 100
            if len(v) > 0:
                mu, std = stats.norm.fit(v)

        if len(v) > 8:
            normal_score, chi = stats.mstats.normaltest(v)

            # Plot the histogram.
            plt.hist(v, bins=50, normed=True, alpha=0.7, color='g')

            # Plot the PDF.
            xmin, xmax = plt.xlim()
            x = np.linspace(xmin, xmax, 100)
            p = stats.norm.pdf(x, mu, std)
            plt.plot(x, p, 'k', linewidth=2)
            title = "Results {}: Mu: %.2f, Std: %.2f, Normal Score: {}" % (mu, std)
            title = title.format(k, normal_score)
            plt.title(title)
            # plt.show()

        print("{:<8} {:<15} {:<15} {:<15} {:<15}".format(k, correct, 100 - correct, mu, std))

    print("There were {} rejections made.".format(rejected))
    print("Of the rejections made, {} would have been identified correctly. ".format(failed_success))

    # print("The following failed: ")
    # for x in fail:
    #     print(x)

    print("Skipped: {}".format(skipped))
