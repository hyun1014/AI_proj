from konlpy.tag import Hannanum

han = Hannanum()

print(han.analyze(u"사과를 먹는다."))
print(han.morphs(u"사과를 먹는다."))
print(han.nouns(u"사과를 먹는다."))
print(han.pos(u"사과를 먹는다.", ntags=9, flatten=True))
print(type(han.analyze(u"사과를 먹는다.")))