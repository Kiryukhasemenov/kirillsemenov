import sqlite3
conn=sqlite3.connect('hittite.db')
c=conn.cursor()

c.executescript('''DROP TABLE IF EXISTS words;
CREATE TABLE IF NOT EXISTS words (id INTEGER PRIMARY KEY AUTOINCREMENT, lemma TEXT, wordform TEXT, glosses TEXT)''')
c.execute('INSERT INTO words (lemma, wordform, glosses) SELECT lemma, wordform, glosses FROM wordforms')
glosschanger=0
idglosses={}
for l in c.execute('SELECT id, glosses FROM words ORDER BY id '):
    id, gloss=l[0], l[1]
    gloss=gloss.split('.')
    gloss=' '.join(gloss)
    idglosses[id]=gloss
sig=sorted(idglosses)
for g in sig:
    c.execute('UPDATE words SET glosses = ? WHERE id = ? ', [idglosses[g], g])
    a=c.fetchall()
with open ('glosses.txt', 'r', encoding='utf-8') as source:
    glosses=source.read()
    glosses=glosses.split('\n')
i=0
newglosses=[]
for g in glosses:
    i+=1
    g=g.split(' — ')
    newg=[]
    newg.append(str(i))
    newg.append(g[0])
    newg.append(g[1])
    newglosses.append(newg)
c.executescript('''DROP TABLE IF EXISTS newglosses;
CREATE TABLE IF NOT EXISTS newglosses (id INTEGER PRIMARY KEY AUTOINCREMENT, glossa TEXT, meaning TEXT)''')
for ng in newglosses:
    c.execute('''INSERT INTO newglosses VALUES (?, ?, ?)''', [ng[0], ng[1], ng[2]])
for a in c.execute('SELECT * FROM newglosses'):
c.execute('SELECT glossa FROM newglosses')
gls=c.fetchall()

gl_to_words=[]
glnum=0
for glsitem in gls:
    glnum+=1
    glsitem=glsitem[0]
    c.execute('SELECT id, glosses FROM words WHERE glosses LIKE ? ', (glsitem,))
    b=c.fetchall()
    bgood=[]
    for bpair in b:
        fortup=[bpair[0], glnum]
        bgood.append(tuple(fortup))
        gl_to_words.append(tuple(fortup))


c.executescript('''DROP TABLE IF EXISTS words_to_glosses;
CREATE TABLE IF NOT EXISTS glosses_summary (glossa_in_text INTEGER, glossa_in_list INTEGER)''')
for gl in gl_to_words:
    c.execute('INSERT INTO glosses_summary VALUES (? , ?) ', [gl[0], gl[1]])
conn.commit()