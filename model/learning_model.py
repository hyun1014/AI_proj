import json
import sys
import nltk
import numpy as np
from keras import models, layers, optimizers, losses, metrics

target = "json_files/" + sys.argv[1] + ".json"
# Loading json file
with open(target) as f:
    train_target = json.load(f)

print(train_target)