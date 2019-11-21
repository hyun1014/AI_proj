from konlpy.tag import Hannanum, Kkma, Komoran, Okt

han = Hannanum()
kma = Kkma()
kom = Komoran()
twit = Okt()

print(han.morphs(u"과제 하기 진짜 싫다. 이번 학기가 얼른 끝났으면 좋겠다."))
print(kma.morphs(u"과제 하기 진짜 싫다. 이번 학기가 얼른 끝났으면 좋겠다."))
print(kom.morphs(u"과제 하기 진짜 싫다. 이번 학기가 얼른 끝났으면 좋겠다."))
print(twit.morphs(u"과제 하기 진짜 싫다. 이번 학기가 얼른 끝났으면 좋겠다."))