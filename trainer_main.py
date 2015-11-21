import os
import pprint
import pickle
from training.trainer import *
from training.training_container import *
from Compare import *
__author__ = 'touma'

container = TrainingContainer()
trainer = ImageTrainer(container)
#image_compare = Comparison()
training_data = ['ones','twos']
for training_dir in training_data:
    trainer.train_directory(os.path.join(os.getcwd(), "data/training/", training_dir),training_dir)

# Output to standard I/O; then ask where to store
#pp = pprint.PrettyPrinter()
#pp.pprint(container.training_lookup)

#container.print_vectors()
feature_vectors=[]
for data in training_data:
    clusters=container.get_clusters_for_key(data)
    image_vectors=[]
    for cluster in clusters:
        image_vectors.append(cluster.vectors['HistogramFeatureExtractor'])
    total_value=[0]*len(image_vectors[0])
    for values in image_vectors:
        for i in range(0,len(image_vectors[0])):
            total_value[i]+=values[i]

    for values in total_value:
        values=values/len(total_value)
    feature_vectors.append(total_value)


#image_compare.process_file(os.path.join(os.getcwd(), "data", ))

print(feature_vectors)
filename = input("Enter filename to store: ")
pickle.dump(feature_vectors, open(filename, "wb"))
