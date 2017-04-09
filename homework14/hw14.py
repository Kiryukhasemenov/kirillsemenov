import re
def s():
    with open ('text1.txt', 'r', encoding='utf-8') as source:
        text=source.read()
        text=text.lower()
    sentences=[]
    sentences=text.split('.')
    nsents=[re.sub(':|,|-|;', '', sentences[i], flags=re.DOTALL) for i in range(len(sentences))]
    return nsents

def word(sents):
    words=[sent.split() for sent in sents]
    return words
##def num():
##def plus(w):
##    for each in w:
##        letnums={}
##        for l in each:
##            letnums[l]=each.count(l)
##    ##    return letnums
##
##        newword=[]
##        for letter in each:
##            n=letnums[letter]
##            print(letter, ' ', n)
##            newlet = "{:{let}<{nl}}"
##            newlet = newlet.format(letter, let=letter, nl=n)        
##            print (newlet)
##            newword.append(newlet)
##        newword=''.join(newword)
##    return newword

def num(w):
   # print(w)
    for sent in w:
        newsent=[]
        for wort in sent:
         #   print(wort)
            letnums={}
            
            newword=[]
            for let in wort:
                letnums[let]=wort.count(let)

                n=letnums[let]
          #     print(let, ' ', n)
                newlet = "{:{l}<{nl}}"
                newlet = newlet.format(let,l=let, nl=n)        
          #      print (newlet)
                newword.append(newlet)
            newword=''.join(newword)
            newsent.append(newword)
       #     print(newword)
        newsent=' '.join(newsent)
        print(newsent)


        
##        newlet = "{:{letnum}<1}"
##        newlet = newlet.format(letter, letnum=letnums[letter])

##        newlet='{:letnums[l]<1}'
##        newlet.format(letter)
    return 'that\`s all!'
num(word(s()))
