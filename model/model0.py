def cutstr(strlist):
    reslist = []
    for onestr in strlist:
        idx = onestr.find("/")
        reslist.append(onestr[:idx])
    return reslist


flist = ['아/Exclamation', '더빙/Noun', '../Punctuation', '진짜/Noun', '짜증나다/Adjective', '목소리/Noun']
print(cutstr(flist))