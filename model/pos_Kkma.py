from konlpy.tag import Kkma

kma = Kkma()

print(kma.morphs(u"이번 학기도 망했다."))
print(kma.nouns(u"이번 학기도 망했다."))
print(kma.pos(u"이번 학기도 망했다.", flatten=True))
print(kma.sentences(u"나는 배가 고프다. 식사를 하러 가자."))
print(kma.sentences(u"아이고 맙소사. 우린 이제 죽었어."))