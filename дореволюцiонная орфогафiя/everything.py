from flask import Flask
from flask import render_template, request
import urllib.request
import re
import os

# def doref(w):
#     wchanging=w
#     changeOrNot=re.search('[ЕеИиФф(ые)сцкнгшщзхвпрлджчмтб]', wchanging)
#     if changeOrNot != None:
#         neww=wchanging
#         idesyat=re.compile(r'(И|и)([аоуыэяёюией])', flags=re.DOTALL)
#         idesyatsearch=re.search(idesyat, wchanging)
#         if idesyatsearch != None:
# #            idesyat.group(0)
# #            idesyatchanger=re.compile(r'i[аоуыэяёюией]', flags=re.DOTALL)
#             neww=re.sub(idesyat,r'i\2',neww)
#             print('!!!'+neww)
#         thetawords=[r'феодор(.*?)', r'анафем(.*?)', r'фимиам(.*?)']#need to change to ѳ
#         for theta in thetawords:
#             onetheta=re.compile(theta, flags=re.DOTALL)
#             thetasearch=re.search(onetheta, wchanging)
#             if thetasearch != None:
#                 neww=re.sub(r'ф',r'ѳ',neww)
#                 print('!!!!!'+neww)
#         yer=re.compile(r'[цкнгшщзхждлрпвфчсмтб]$', flags=re.DOTALL)
#         yersearch=re.search(yer, wchanging)
#         if yersearch != None:
#             neww=re.sub(r'$', r'ъ', neww)
#             print('!!!!!!!!!!!!!!!!!!'+neww)
#         prefix=re.compile(r'\b(и|(во)|(ра)|(бе)|(ни)|в)?с.*?', flags=re.DOTALL)
# #        oldprefix=re.compile(r'(и|(во)|(ра)|(бе)|(ни)|в)?з.*?', flags=re.DOTALL)
#         prefixsearch=re.search(prefix, wchanging)
#         if prefixsearch != None:
#             neww=re.sub(prefix, r'\1з', neww)
#             print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'+neww)
#         print('doref.word detected')
#     else:
#         print('???'+wchanging)
#     return 'fuck off'
# doref('расстаться')

def mystem1(w):
    with open('input.txt', 'w', encoding='utf-8') as source1:
        source1.write(w)
    os.system("C:\\Users\\lenovo\\Desktop\\mystem.exe -nid input.txt output.txt")
    with open('output.txt', 'r', encoding='utf-8') as source2:
        text=source2.read()
    print('mystem1: '+text)
    return(text)
#mystem1('мыши')
def mystem2(m1):
    lemma=re.compile(r'{(.*?)=', flags=re.DOTALL)
    lemmasearch=re.search(lemma, m1)
    if lemmasearch != None:
        neededlemma=lemmasearch.group(1)
    print('mystem2: '+neededlemma)
    return neededlemma
def mystem3(a):
    databl=re.compile(r'од=(пр)|(дат),', flags=re.DOTALL)
    datablsearch=re.search(databl, a)
    if datablsearch !=None:
        return '+databl'
    else:
        return '-databl'

#mystem2(mystem1('мыши'))
def dictopen():
    with open('dict.csv', 'r', encoding='utf-8') as source3:
        dictUlt=source3.read()
        dictUlt=dictUlt.split('\n')
#        print(dictUlt)
    dict={}
    for d in dictUlt:
        d=d.split(',')
#        print(d)
        if len(d)==2:
            rus, old=d[0], d[1]
            dict[rus]=old
#    print(dict)
    return dict
def firstcheck(w):
    dorwords=dictopen()
    print('input: '+w)
    if w in dorwords:
#        print(dorwords[w])
        return dorwords[w]
    else:
        infinite=mystem2(mystem1(w))
        quasibase=[]
        quasiending=[]
        wlist=list(w)
        infinitelist=list(infinite)
#        print(wlist)
#        print(infinitelist)
        j=len(infinitelist)-1
        for i in range(len(wlist)):
            if i<=j:
#                print(i)
#            print(i)
                if wlist[i]==infinitelist[i]:
                    quasibase.append(wlist[i])
                else:
                    quasiending.append(wlist[i])
            else:
                quasiending.append(wlist[i])
        quasibase=''.join(quasibase)
        qb=len(quasibase)
        quasiending=''.join(quasiending)
        if infinite in dorwords:
            dorquasibase=dorwords[infinite][:qb]
#            print(dorquasibase)
#            print(quasiending)
            da=mystem3(mystem1(w))
            if da=='+databl' and quasiending =='е':
                quasiending='ѣ'
            finalword=dorquasibase+quasiending

        else:
            print('totally another, still okay: '+w)
            da = mystem3(mystem1(w))
            if da == '+databl' and quasiending == 'е':
                quasiending = 'ѣ'
                dorquasibase=w[:-1]
                finalword = dorquasibase + quasiending
            else:
                finalword=w
#            finalword = dorquasibase + quasiending
        print ('other word detected')
#    finalword=dorquasibase+quasiending
    print('first check done: '+finalword)
    return finalword

#firstcheck('доме')
def seccheck(f):
    wchanging = f
    print('input from 1 check: '+wchanging)
    changeOrNot = re.search('[ЕеИисцкнгшщзхвпрлджчмтб]', wchanging)
    if changeOrNot != None:
        neww = wchanging
        idesyat = re.compile(r'(И|и)([аоуыэяёюией])', flags=re.DOTALL)
        idesyatsearch = re.search(idesyat, wchanging)
        if idesyatsearch != None:
            #            idesyat.group(0)
            #            idesyatchanger=re.compile(r'i[аоуыэяёюией]', flags=re.DOTALL)
            neww = re.sub(idesyat, r'i\2', neww)
#            print('!!!' + neww)
        yer = re.compile(r'[цкнгшщзхждлрпвфчсмтб]$', flags=re.DOTALL)
        yersearch = re.search(yer, wchanging)
        if yersearch != None:
            neww = re.sub(r'$', r'ъ', neww)
#            print('!!!!!!!!!!!!!!!!!!' + neww)
        prefix = re.compile(r'\b(и|(во)|(ра)|(бе)|(ни)|в|(ч(е)?рез))?с.*?', flags=re.DOTALL)
        #        oldprefix=re.compile(r'(и|(во)|(ра)|(бе)|(ни)|в)?з.*?', flags=re.DOTALL)
        prefixsearch = re.search(prefix, wchanging)
        if prefixsearch != None:
            neww = re.sub(prefix, r'\1з', neww)
 #           print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!' + neww)
  #      print('doref.word detected')
    else:
        neww=wchanging
  #      print('???' + wchanging)
    print('end of the second check: '+neww)
    return neww
#seccheck(firstcheck('адомантия'))
def weather():
    req = urllib.request.Request('https://yandex.ru/pogoda/10463')
    with urllib.request.urlopen(req) as response:
        code = response.read().decode('UTF-8')
    reg=re.search('<span class="temp__value">(.*?)</span>', code, flags=re.DOTALL)
    current_weather=reg.group(1)
    return current_weather

app = Flask(__name__)

@app.route('/translate')
def translate():
    temperature = weather()
    if request.args:
        word=request.args['word']
        print('lsfdhkf '+word)
        newword=seccheck(firstcheck(word))
        print('!!!!!')
        print('this must be new '+newword)
        return render_template('form.html', newword=newword, temperature=temperature)
    return render_template('form.html', temperature=temperature)

@app.route('/oldschool')
def oldschool():
    return render_template('oldschool.html')

@app.route('/test')
def test():
    return render_template('test.html')

if __name__ == '__main__':
    app.run(debug=True)
