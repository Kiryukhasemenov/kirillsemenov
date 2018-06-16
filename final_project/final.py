from flask import Flask
from flask import render_template, request
import re
from random import uniform
from collections import defaultdict

r_alphabet = re.compile(u'[а-яА-Я0-9-]+|[.,:;?!]+')

def propers(corpus):
    with open (corpus, 'r', encoding='utf-8') as src:
        lines=src.readlines()
    proper_names=[]
    for line in lines:
        proper=re.findall(r'[a-яА-Я] [А-Я][а-я]+', line, flags=re.DOTALL)
    #print()
        for p in proper:
            proper_names.append(p[2:].lower())
    return proper_names
	
def gen_lines(corpus):
#    data = open(corpus)
#    for line in data:
#        yield line.decode('utf-8').lower()
    with open(corpus, 'r', encoding='utf-8') as src:
        data=src.readlines()
    #data = open(corpus)
    for line in data:
        yield line.lower()

def gen_tokens(lines):
    for line in lines:
        for token in r_alphabet.findall(line):
            yield token

def gen_trigrams(tokens):
    t0, t1 = '$', '$'
    for t2 in tokens:
        yield t0, t1, t2
        if t2 in '.!?':
            yield t1, t2, '$'
            yield t2, '$','$'
            t0, t1 = '$', '$'
        else:
            t0, t1 = t1, t2

def train(corpus):
    lines = gen_lines(corpus)
    tokens = gen_tokens(lines)
    trigrams = gen_trigrams(tokens)

    bi, tri = defaultdict(lambda: 0.0), defaultdict(lambda: 0.0)

    for t0, t1, t2 in trigrams:
        bi[t0, t1] += 1
        tri[t0, t1, t2] += 1

    model = {}
    for (t0, t1, t2), freq in tri.items():
        if (t0, t1) in model:
            model[t0, t1].append((t2, freq/bi[t0, t1]))
        else:
            model[t0, t1] = [(t2, freq/bi[t0, t1])]
    return model

def unirand(seq):
    sum_, freq_ = 0, 0
    for item, freq in seq:
        sum_ += freq
    rnd = uniform(0, sum_)
    for token, freq in seq:
        freq_ += freq
        if rnd < freq_:
            return token

def not_rand(text):
    seq=input('Введите предложение ').split()
    sum_, freq_ = 0,0
    for item, freq in seq:
        sum_+= freq
    rnd = uniform(0, sum_)
    for token, freq in seq:
        freq_ += freq
        if rnd < freq_:
            return token
def generate_sentence(model):
    phrase = ''
    t0, t1 = '$', '$'
    while 1:
        t0, t1 = t1, not_rand(model[t0, t1])
        if t1 == '$': break
        if t1 in ('.!?,;:') or t0 == '$':
            phrase += t1
        else:
            phrase += ' ' + t1
    return phrase.capitalize()

def input_sentence(s):
    
    a=s.lower()
    a=a.split()
    return a

model=train('lt1.txt')
all_names=propers('lt1.txt')

def gen_sent(inp, mod, n):
    phrase = ''
    
    if len(inp)==1:
        t0, t1= '$', inp[0]
        phrase='...'+t1+' '
    else:
        t0, t1= inp[-2], inp[-1]
        phrase='...'+t0+' '+t1
    while t1 != '$':
        try:
            t0, t1=t1, unirand(model[t0, t1])
        except:
            t0, t1 = '$', '$'
            t0, t1=t1, unirand(model[t0, t1])
        if t1 in ('.!?,;:') or t0 == '$':
            phrase += t1
        else:
            if t1 != '$':
                if t1 not in n:
                    print('result 3')
                    phrase += ' ' + t1
                else:
                    print('result 4')
                    t1_new=t1.capitalize()
                    print(t1_new)
                    phrase += ' ' + t1_new
    phrase=phrase.capitalize()
    print(phrase)
    return phrase
#model = train('tolstoy.txt')
#for i in range(10):
#    print (generate_sentence(model))
app = Flask(__name__)

@app.route('/')
def index():
    if request.args:
        old_sentence=request.args['old_sentence']
        new_sentence=gen_sent(input_sentence(old_sentence), model, all_names)#вот тут надо поменять
        return render_template('form1.html', old_sentence=old_sentence, new_sentence=new_sentence)
    return render_template('form1.html')
if __name__ == '__main__':
    app.run(debug=True)
#if __name__ == '__main__':
#    import os
#    app.debug = True
#    port = int(os.environ.get("PORT", 5000))
#    app.run(host='0.0.0.0', port=port)