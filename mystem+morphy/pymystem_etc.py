from pymorphy2 import MorphAnalyzer
morph = MorphAnalyzer()
from pymystem3 import Mystem
def parser(s):
    s=s.strip('!?.,:;"')
    sentence=s.split()
    return sentence
#parser('Мама мыла раму')
def first_proc(s):
    result=[]
    for s_item in s:
        ana=morph.parse(s_item)
        print(ana)
        result.append(ana)
    return result
def null_proc(s):
    m=Mystem()
    res=[]
    s=m.lemmatize(s)
    for w in s:
        if w != ' ' and w !='\n':
            res.append(w)
    return res
def skryzh(s):
    words=parser(s)
    lemmas=null_proc(s)
    variants=first_proc(words)
    needed_info=[]
    #print(variants)
    for i in range(len(words)):
        #print('look')
        #print(variants[i])
        for var in variants[i]:
            #print(var)
            if var.normal_form==lemmas[i]:
                needed_info.append(var)
    return needed_info
def dict_opener():
    source_list=[]
    with open ('lemma.txt', 'r', encoding='utf-8') as source:
        data=source.readlines()
    dict_with_pos={}
    for line in data:
        line=line.split()
        pos=line[3].upper()
        pos=conformity(pos)
        if pos not in dict_with_pos:
            #pos=line[3].upper()
            dict_with_pos[pos]=[]
            #print(dict_with_pos[pos])
            dict_with_pos[pos].append(line[2])
            #print(dict_with_pos[pos])
        else:
            dict_with_pos[pos].append(line[2])
            #print(dict_with_pos[pos])
        #source_list.append(line[2])
    return dict_with_pos
def dict_opener_2():
    words_with_char={}
    chars_with_words={}
    with open ('lemma.txt', 'r', encoding='utf-8') as source:
        data=source.readlines()
    for line in data:
        line=line.split()
        lemma=line[2]
        chars=morph.parse(lemma)[0]
        chars=str(chars.tag)
        chars=chars.split(' ')
        chars=chars[0]
        words_with_char[lemma]=chars
        if chars not in chars_with_words:
            chars_with_words[chars]=[lemma]
        else:
            chars_with_words[chars].append(lemma)
    return chars_with_words
def conformity(l):
    matches={'NOUN':'NOUN', 'MISC':'PRCL', 'PREP':'PREP','PRON':'NPRO', 'ADJPRON':'ADJF','VERB':'VERB','ADV':'ADVB', 'CARD':'NUMR', 'ADJ':'ADJF','ORD':'ADJF'}
    lnew=matches[l]
    return lnew
def final_1(f):
    grammar=[]
    for f_el in f:
        a=str(f_el.tag)
        #a=a.OpencorporaTag.value()
        a=a.split(' ')
        #a[0]=a[0].split(',')[0]
        grammar.append(a)
    return grammar
def chooser(c):
    import random
    new_lemmas=[]
    source_dict=dict_opener_2()
    for c_item in c:
        new_lemma=random.choice(source_dict[c_item[0]])
        new_lemmas.append(new_lemma)
    return new_lemmas
def prefinal_inflector(f):
    grammemes=[]
    for f_item in f:
        grammeme=str(f_item.tag)
        grammeme=grammeme.split(' ')[1]
        grammemes.append(grammeme)
    return grammemes
def final(f1, f2):
    lemmas=f1
    grammemes=f2
    final_sentence=[]
    for i in range(len(lemmas)):
        print(lemmas[i])
        newword=morph.parse(lemmas[i])[0]
        #print(word)
        print(grammemes[i])
        grams=grammemes[i].split(',')
        for g in grams:
            newword=newword.inflect({g})
        newword=str(newword.word)
        #print(word)
        final_sentence.append(newword)
    final_sentence=' '.join(final_sentence)
    return final_sentence

from flask import Flask
from flask import render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    if request.args:
        old_sentence=request.args['old_sentence']
        new_sentence=final(chooser(final_1(skryzh(old_sentence))),prefinal_inflector(skryzh(old_sentence)))
        return render_template('form1.html', new_sentence=new_sentence)
    return render_template('form1.html')

if __name__ == '__main__':
    app.run(debug=True)

