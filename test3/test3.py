def readpage():
    with open ('site.txt', 'r', encoding='utf-8') as source:
        text=source.read()
        tokens=text.split()
        bare_tokens=[]
        for i in range(len(tokens)):
            token=tokens[i]
            token=token.strip(',!?");:|—')
            bare_tokens.append(token)
        newtext=' '.join(bare_tokens)
    return newtext

import re
def initials(a):
 #   newtext=' '.join(a)
 #   inits='\s[А-Я]\. [А-Я].*?\s'
    results=re.findall(r'\s[А-ЯA-Z]\. [А-ЯA-Z][^\.].*?\s', a)
    print('Задание №1')
    return results



def all_names(a):
    print('Задание №2')
    init_names=re.findall(r'\s[А-ЯA-Z]\. [А-ЯA-Z]?\.? [А-ЯA-Z][^\.].*?\s', a)

    full_names=re.findall(r'\s[А-ЯA-Z][^\.]\w+ [А-ЯA-Z][^\.].*?\s', a)

    triple_names=re.findall(r'\s[А-ЯA-Z][^\.]\w+ [А-ЯA-Z][^\.]\w+ [А-ЯA-Z][^\.].*?\s', a)
   # all_of_them.append(triple_names)
    all_of_them=[init_names, full_names, triple_names]
    new_all=[item for arr in all_of_them for item in arr]
    return new_all


