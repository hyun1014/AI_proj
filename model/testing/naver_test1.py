import json
import os
from konlpy.tag import Okt
from pprint import pprint
import nltk
import numpy as np
from keras import models, layers, optimizers, losses, metrics


def cutstr(strr):
    idx = strr.find("/")
    return strr[0:idx]


def read_data(filename):
    with open(filename, 'r') as f:
        data = [line.split('\t') for line in f.read().splitlines()]
        data = data[1:]
    return data


def tokenize(doc):
    # 조사 종류는 제거함
    return [t[0] for t in Okt().pos(doc, norm=True, stem=True)]


# Read raw dataset from .txt file
train_data = read_data("../../ratings_train_shorten.txt")
test_data = read_data("../../ratings_test_shorten.txt")

if os.path.isfile("train_docs.json"):
    # If train_docs.json exists in current directory, make a list from the json
    with open("train_docs.json") as f:
        train_docs = json.load(f)
    with open("test_docs.json") as f:
        test_docs = json.load(f)
else:
    # Make a list of data with tokenized sentences and result
    train_docs = [[tokenize(row[1]), row[2]] for row in train_data]
    test_docs = [[tokenize(row[1]), row[2]] for row in test_data]
    # Save as json file
    with open("train_docs.json", "w", encoding="utf-8") as make_file:
        json.dump(train_docs, make_file, ensure_ascii=False, indent="\t")
    with open("test_docs.json", "w", encoding="utf-8") as make_file:
        json.dump(test_docs, make_file, ensure_ascii=False, indent="\t")

# First row which has a list of tokens and a result
pprint(train_docs[0])
# Show only a list of tokens
print(train_docs[0][0])

# Make a list of tokens
train_tokens = [t for d in train_docs for t in d[0]]
test_tokens = [t for d in test_docs for t in d[0]]
# Number of tokens
print(len(train_tokens))
print(len(test_tokens))

# Use nltk.Text module to make a set (중복 제거)
train_text = nltk.Text(train_tokens, name="train_t")
test_text = nltk.Text(test_tokens, name="test_t")
# 중복 제거
print(len(set(train_text.tokens)))
print(len(set(test_text.tokens)))

# Make a list of the most commonly appeared tokens. (token, counts of appeared)
pprint(train_text.vocab().most_common(10))
pprint(test_text.vocab().most_common(10))
print(train_text.vocab().most_common(10)[0])

# Only tokens, except result
selected_words = [f[0] for f in train_text.vocab().most_common(10)]
print(selected_words)


# selected_words 안에 있는 word들이 각각 얼마나 나왔나
def term_frequency(doc):
    return [doc.count(word) for word in selected_words]


# Vectorization
# x is input (term), and it is dataset
train_x = [term_frequency(d) for d, _ in train_docs]
test_x = [term_frequency(d) for d, _ in test_docs]
# y is output (0 or 1), and it is dataset
train_y = [c for _, c in train_docs]
test_y = [c for _, c in test_docs]
print(len(train_x))

# Change x and y to float type data
x_train = np.asarray(train_x).astype("float32")
x_test = np.asarray(test_x).astype("float32")
y_train = np.asarray(train_y).astype("float32")
y_test = np.asarray(test_y).astype("float32")
print(len(x_train))

print(train_x)
print(x_train)
