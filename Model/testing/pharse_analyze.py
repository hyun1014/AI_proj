import nltk
from konlpy.tag import Okt

twit = Okt()
sentence = u"만 19세 미만 청소년은 관람이 불가합니다."
words = twit.pos(sentence)

gram = """
NP: {<N.*>*<Suffix>?}   # Noun phrase
VP: {<V.*>*}            # Verb phrase
AP: {<A.*>*}            # Adjective phrase
"""

print(gram)
parser = nltk.RegexpParser(gram)
chunks = parser.parse(words)
print("Whole trees")
print(chunks.pprint())

print("Only nouns")
for subtree in chunks.subtrees():
    if subtree.label()=="NP":
        print(' '.join(e[0] for e in list(subtree)))
        print(subtree.pprint())

