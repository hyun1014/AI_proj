import json
import sys
import nltk
import datetime
import numpy as np
from keras import models, layers, optimizers, losses, metrics


target = "json_files/ratings_train_dset.json"
# Loading json file
with open(target) as f:
    train_target = json.load(f)

# Only tokens
train_tokens = [tok for d in train_target for tok in d[0]]
train_text = nltk.Text(train_tokens, name="train_t")

# Make selected_word <- This is used to make vector
common_tests = train_text.vocab().most_common(100)
selected_word = [word[0] for word in common_tests]


def term_frequency(doc):
    return [doc.count(s_word) for s_word in selected_word]


# Vectorization
# x is input (term), and it is dataset
train_x = [term_frequency(d) for d, _ in train_target]
# y is output (0 or 1), and it is dataset
train_y = [c for _, c in train_target]

# Change x and y to float type data
train_x = np.asarray(train_x).astype("float32")
train_y = np.asarray(train_y).astype("float32")

# Initialize model
model = models.Sequential()
# Add layers to model(Output size, activation function, input size)
model.add(layers.Dense(64, activation="relu", input_shape=(100,)))
model.add(layers.Dense(64, activation="relu"))
model.add(layers.Dense(1, activation="sigmoid"))
# Set method of learning and evaluation (Gradient descent, error function, evaluation indicator)
model.compile(optimizer=optimizers.RMSprop(lr=0.001),
              loss=losses.binary_crossentropy,
              metrics=[metrics.binary_accuracy])

# Start learning (Input, output, number of trial, size of input at once
model.fit(train_x, train_y, epochs=100, batch_size=1024)
print("Learning complete.")

# Save model
c_time = datetime.datetime.now()
cur_time = c_time.strftime("%Y_%m_%d_%H_%M_%S__")
model_name = "NLP_model/learned_model_prototype4_1.h5"
model.save(model_name)
# Save selected_word in json file
with open("NLP_model/selected_word_prototype4_1.json", "w") as sf:
    json.dump(selected_word, sf, ensure_ascii=False)
print("Model is saved.")
