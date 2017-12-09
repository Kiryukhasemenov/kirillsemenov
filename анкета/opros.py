from flask import Flask
from flask import render_template, request
import json


def json1(ad):
    json_string = json.dumps(ad, ensure_ascii=False, sort_keys=True, indent=4)
    with open('all_answers.json', 'w', encoding='utf-8') as source:
        source.write(json_string)
    return json_string


def extract():
    json1(dictmaker(opener()))
    with open('all_answers.json', 'r', encoding='utf-8') as source1:
        data=source1.read()
        data=json.loads(data)
        return data



def res1(a, b):
    d=extract()
    allgests=[]
    for i in d:
        if i['language'] == a:
            allgests.append(i[b])
    return allgests



app = Flask(__name__)

@app.route('/')
def index():
    if request.args:
        name=request.args['pname']
        gender=request.args['gender']
        age=request.args['age']
        country=request.args['country']
        lang=request.args['language']
        gest38=request.args['gesture38']
        gest39=request.args['gesture39']
        gest67=request.args['gesture67']
        gest68=request.args['gesture68']
        with open('results.txt', 'a', encoding='utf-8') as source:
            source.write(name+';'+gender+';'+age+';'+country+';'+lang+';'+gest38+';'+gest39+';'+gest67+';'+gest68+'\n')
        json1(dictmaker(opener()))
    return render_template('form1.html')

def opener():
    with open('results.txt', 'r', encoding='utf-8') as source:
        src=source.readlines()
    return src

def dictmaker(s):
    alldicts=[]
    keys=['name','gender','age','country','language','gest38','gest39','gest67','gest68']
    for line in s:
        lildct={}
        chars=line.split(';')
        for i in range(len(chars)):
            lildct[keys[i]]=chars[i]
        alldicts.append(lildct)
    return alldicts

def json1(ad):
    json_string = json.dumps(ad, ensure_ascii=False, sort_keys=True, indent=4)
    with open('all_answers.json', 'w', encoding='utf-8') as source:
        source.write(json_string)
    return json_string


@app.route('/stats')
def statistics():
    d=extract()
    langvals={}
    agesum=0
    agenum=0
    countryvals={}
    for l in d:
        agenum+=1
        agesum+=int(l['age'])
        avage=str(agesum//agenum)
        langcountries = []
        if l['language'] not in langvals:
            langvals[l['language']]=1
            countryvals[l['language']]=[l['country']]
        else:
            langvals[l['language']]+=1
            if l['country'] not in countryvals[l['language']]:
                countryvals[l['language']].append(l['country'])
        langcountries=' '.join(langcountries)
        print(langcountries)
    print(countryvals)
    return render_template('stats.html', langvals=langvals, avage=avage, countryvals=countryvals)

@app.route('/json')
def javawork():
    a=dictmaker(opener())
    newa=json.dumps(a, ensure_ascii=False, sort_keys=True, indent=4)
    return newa

@app.route('/search')
def dosearch():
    if request.args:
        searchlang=request.args['searchlang']
        searchgest=request.args['searchgest']
        gests=res1(searchlang, searchgest)
        return render_template('results.html', searchlang=searchlang, searchgest=searchgest, gests=gests)
    return render_template('search.html')


if __name__ == '__main__':
    app.run(debug=True)
