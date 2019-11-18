from konlpy.corpus import kolaw

f_ids = kolaw.fileids()
f_obj = kolaw.open(f_ids[0])

print(f_ids)
