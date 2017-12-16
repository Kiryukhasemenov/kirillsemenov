import sqlite3
import matplotlib
import matplotlib.pyplot as plt

# pronouns have glossa PRON
#verbs usually have PST, PRS, PRT, IMF
#there is also ENCL, which can be combined with RPON
#nouns are not marked, only with number and case
conn=sqlite3.connect('hittite.db')
c=conn.cursor()
all_data=[]
pronglosses=[]
dictpronglosses={}
dictverbglosses={}
for a in c.execute('SELECT glosses FROM words'):
    print(a)
    all_data.append(a)
    oneglossa=a[0].split(' ')
    if "PRON" in oneglossa:
        for o in oneglossa:
            if o!="PRON" and o.lower() != o:
                if o not in dictpronglosses:
                    dictpronglosses[o]=1
                else:
                    dictpronglosses[o]+=1
    elif "PST" in oneglossa or "PRS" in oneglossa or "PRT" in oneglossa or "IMF" in oneglossa:
        for o in oneglossa:
            if o.lower() !=o:
                if o not in dictverbglosses:
                    dictverbglosses[o]=1
                else:
                    dictverbglosses[o]+=1
conn.commit()

verbx=[]
verby=[]
for verbglossa in sorted(dictverbglosses):
    verbx.append(verbglossa)
    verby.append(dictverbglosses[verbglossa])
verbxaxis=[a for a in range(1, len(verbx)+1)]
plt.title('Verb glosses')
plt.xlabel('Glossa')
plt.ylabel('Number of tokens')
for x, y, gl in zip(verbxaxis, verby, verbx):
    plt.bar(x, y)
    plt.text(x-0.5, y+0.2, gl)
plt.show()
pronitems=[]
prony=[]
for pronglossa in sorted(dictpronglosses):
    pronitems.append(pronglossa)
    prony.append(dictpronglosses[pronglossa])
pronx=[b for b in range(1, len(pronitems)+1)]
plt.title('Pronoun glosses')
plt.xlabel('Glossa')
plt.ylabel('Number of tokens')
for x, y, gl in zip(pronx,prony,pronitems):
    plt.bar(x,y)
    plt.text(x-0.5, y+0.2, gl)
plt.show()