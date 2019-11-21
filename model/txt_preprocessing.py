from konlpy.tag import Okt
import json
import datetime
import sys

c_time = datetime.datetime.now()
cur_time = c_time.strftime("%Y_%m_%d_%H_%M_%S__")
parser = Okt()


# Read txt file
def read_data(txt_file):
    with open(txt_file, "r") as f:
        raw_data = f.read().splitlines()
        data = [line.split("\t") for line in raw_data]
        data = data[1:]
    return data


# Only word, except josa
def tokenize(doc):
    return [t[0] for t in parser.pos(doc, norm=True, stem=True)]


# Read data and put it to raw_doc
target = "txt_files/" + sys.argv[1] + ".txt"
raw_doc = read_data(target)

# Tokenized words and output result(0 or 1)
data_set = [[tokenize(doc[1]), doc[2]] for doc in raw_doc]

# Make a json file
file_name = "json_files/" + sys.argv[1] + "_dset.json"
with open(file_name, "w") as make_file:
    json.dump(data_set, make_file, ensure_ascii=False, indent="  ")

print("Preprocessing complete.")