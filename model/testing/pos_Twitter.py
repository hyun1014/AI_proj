from konlpy.tag import Okt

# Twitter has been changed to Okt since "konlpy" 0.4.5

twit = Okt()

print(twit.morphs(u"이 짓을 언제까지 하는 것일까."))
print(twit.nouns(u"양꼬치와 맥주를 먹고 싶다."))
print(twit.phrases(u"오늘은 힘세고 강한 아침이다."))
print(twit.pos(u"이것도 가능한가 진짴ㅋㅋㅋㅋㅋㅋ"))
print(twit.pos(u"이것도 가능한가 진짴ㅋㅋㅋㅋㅋㅋ", norm=True))
print(twit.pos(u"이것도 가능한가 진짴ㅋㅋㅋㅋㅋㅋ", norm=True, stem=True))
