from konlpy.tag import Komoran

kom = Komoran()

print(kom.morphs(u"집에 가고 싶다."))
print(kom.nouns(u"집에 가고 싶다."))
print(kom.pos(u"집에 가고 싶다.", flatten=True))
