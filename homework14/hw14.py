import re
def s():
    with open ('text1.txt', 'r', encoding='utf-8') as source:
        text=source.read()
        text=text.lower()
    sentences=[]
    sentences=text.split('.')
    nsents=[re.sub(':|,|-|;', '', sentences[i], flags=re.DOTALL) for i in range(len(sentences))]
##    for i in range(len(sentences)):
##        sent=sentences[i] 
##        nsent=re.sub(':|,|-', '', sent, flags=re.DOTALL)
##        nsents.append(nsent)
##    sents=[i.strip(',-') for i in sentences]
    return nsents
def gain(sents):
    words=[sent.split() for sent in sents]
##    for l in range(len(words[i])):
##        if l not in words[i]:
##            letters.append(l)
##        else
    for word in words:
        letters=list(word)
        l_freq={}
##    
##    for sent in range(len(sents)):
##        words=sent.split()
    return words
