import os
import pprint
import pickle
from training.trainer import *
from training.training_container import *

__author__ = 'touma'

container = TrainingContainer()
trainer = ImageTrainer(container)

training_data = ['noto']

for training_dir in training_data:
    trainer.train_directory(os.path.join(os.getcwd(), "data/training/", training_dir))

# Output to standard I/O; then ask where to store
pp = pprint.PrettyPrinter()
pp.pprint(container.training_lookup)

filename = input("Enter filename to store: ")
pickle.dump(container, open(filename, "wb"))
