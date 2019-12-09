import json
import sys
import numpy as np
from keras.models import load_model


target_model = "NLP_model/learned_model.h5"
target_json = "json_files/ratings_test_dset.json"
# Load json file for test
with open(target_json) as f:
    test_target = json.load(f)

# Load selected_word
with open("NLP_model/selected_word.json", "r") as sf:
    selected_word = json.load(sf)
# Load model
model = load_model(target_model)


def term_frequency(doc):
    return [doc.count(s_word) for s_word in selected_word]


# Vectorization
# x is input (term), and it is dataset
test_x = [term_frequency(d) for d, _ in test_target]
# y is output (0 or 1), and it is dataset
test_y = [c for _, c in test_target]

# Change x and y to float type data
test_x = np.asarray(test_x).astype("float32")
test_y = np.asarray(test_y).astype("float32")

# Evaluate model with test dataset
result = model.evaluate(test_x, test_y)
test_accuracy = result[1] * 100
print("Accuracy is {:.2f}%".format(test_accuracy))
