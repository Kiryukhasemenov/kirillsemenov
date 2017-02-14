import re
def file_opener():
    with open ('corpus.txt', 'r', encoding='utf-8') as corpus:
        words=corpus.readlines()
    return words
def f1(lines):
    lines_num=int()
    for line in lines:
        lines_num+=1
    with open ('lines_number.txt', 'a', encoding='utf-8') as firstdoc:
        firstdoc.write(str(lines_num))
    return 'The first answer is in the "lines_number" document.'
def f2(lines):
    grlist=[]
    word_charact=r'<w\stype="(.*?)"\slemma='
    for line in lines:
        result=re.search(word_charact, line)
        if result !=  None:
            gram=result.group(1)
            grlist.append(gram)
    isl_dict={}
    for gr in grlist:
        if gr in isl_dict:
            isl_dict[gr]+=1
        else:
            isl_dict[gr]=1
    with open ('grammemes.txt', 'a', encoding='utf-8') as secdoc:
        for grammeme in isl_dict:
            secdoc.write(grammeme+'\n')
    return 'The second answer is in the "grammemes" document.'
##def f3(lines):
    

def fin():
    return f1(file_opener()) + ' ' + f2(file_opener())

fin()
