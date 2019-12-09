import json
import numpy as np
from konlpy.tag import Okt
from keras.models import load_model

parser = Okt()
target_model = "NLP_model/learned_model.h5"

# Load selected_word
with open("NLP_model/selected_word.json", "r") as sf:
    selected_word = json.load(sf)
# Load model
model = load_model(target_model)


def tokenize(sentence):
    list = [t[0] for t in parser.pos(sentence, norm=True, stem=True)]
    return list


# selected_word 안에 있는 word들이 각각 얼마나 나왔나
def term_frequency(doc):
    return [doc.count(word) for word in selected_word]


def calculate_sentiment_single_diary(sent):
    tokens = tokenize(sent)
    tf = term_frequency(tokens)
    data = np.expand_dims(np.asarray(tf).astype("float32"), axis=0)
    score = float(model.predict(data))
    if score > 0.5:
        return 1
    else:
        return 0


# This is for test mode. 6 sentences can be evaluated.
if __name__ == "__main__":
    print("Test mode\n\n")
    for i in range (6):
        sent = input("문장을 입력하세요.\n")
        res = calculate_sentiment_single_diary(sent)
        if res==1:
            print("\n입력 문장: " + sent + "\n긍정적인 감정의 문장입니다.\n")
        else:
            print("\n입력 문장: " + sent + "\n부정적인 감정의 문장입니다.\n")
    print("Test is completed.\n")
