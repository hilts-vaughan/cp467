import os
import pprint
import pickle
from training.trainer import *
from training.training_container import *

def trainer_main():
    container = TrainingContainer()
    trainer = ImageTrainer(container)
    #image_compare = Comparison()
    training_data = ['zeros', 'ones', 'twos', 'threes', 'fours', 'fives', 'sixs', 'sevens', 'eights', 'nines']
    for training_dir in training_data:
        trainer.train_directory(os.path.join(os.getcwd(), "data/training/", training_dir),training_dir)

    # Output to standard I/O; then ask where to store
    #pp = pprint.PrettyPrinter()
    #pp.pprint(container.training_lookup)

    #container.print_vectors()

    feature_vectors = {}

    expected_clusters = ['HistogramFeatureExtractor', 'WeightedVectorsFeatureExtractorX', 'WeightedVectorsFeatureExtractorY', 'ZoningFeatureExtractor']

    for data in training_data:
        clusters = container.get_clusters_for_key(data)
        feature_vectors[data] = {}
        for expected_cluster in expected_clusters:

            image_vectors = []
            for cluster in clusters:
                image_vectors.append(cluster.vectors[expected_cluster])
            total_value=[0]*len(image_vectors[0])

            for values in image_vectors:
                for i in range(0,len(image_vectors[0])):
                    total_value[i] += values[i]

            for i in range (0, len(total_value)):
                total_value[i] = total_value[i]/len(image_vectors)

            feature_vectors[data][expected_cluster] = total_value


    #image_compare.process_file(os.path.join(os.getcwd(), "data", ))

    print(feature_vectors)
    filename = input("Enter filename to store: ")
    pickle.dump(feature_vectors, open(filename, "wb"))
