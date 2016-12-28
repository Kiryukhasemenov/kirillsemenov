import random
def subject():
    with open('nouns.txt', 'r', encoding='utf-8') as source:
        lines=source.read()
##        sg_nouns=lines[0].split()
##        pl_nouns=lines[1].split()
        nouns=lines.split()
##        print(sg_nouns)
##        print(pl_nouns)
##    sg_subject=random.choice(sg_nouns)
##    pl_subject=random.choice(pl_nouns)
    subject=random.choice(nouns)
    return subject
def transitive_verb(subj):
    with open('transitive_verbs.txt', 'r', encoding='utf-8') as source2:
##        line=source2.read()
##        tr_verbs=line.split()
        lines=source2.readlines()
        verbs_sg=lines[0].split()
        verbs_pl=lines[1].split()
    if subj[-1]=='и' or subj[-1]=='ы':
        return random.choice(verbs_pl)
    else:
        return random.choice(verbs_sg)
##    tr_verb=random.choice(tr_verbs)
##    return tr_verb
def noun_phrase(subj):
    with open('adjectives.txt', 'r', encoding='utf-8') as source3:
        lines=source3.readlines()
        m_adj=lines[0].split()
        f_adj=lines[1].split()
    if subj[-1]=='а' or subj[-1]=='я':
        return random.choice(f_adj) + ' ' + subj
    else:
        return random.choice(m_adj) + ' ' + subj
def adverb():
    with open('adverbs.txt', 'r', encoding='utf-8') as source4:
        line=source4.read()
        advs=line.split(', ')
    return random.choice(advs)
def intransitive_verb():
    with open('intransitive_verbs.txt', 'r', encoding='utf-8') as source5:
        line=source5.read()
        intr_verbs=line.split()
    return random.choice(intr_verbs)
def sent1():
    sent='Уж ' + adverb() + ' ' + intransitive_verb() + ' ' + noun_phrase(subject()) + ', a ' + subject() + ' все ' + intransitive_verb() + '...'
    return sent.capitalize()
def satzgefuege():
    sent=0
    return sent
def sent2():
    sent=transitive_verb(subject()) + '!'
    return sent.capitalize()
##import random
##def subject():
##    with open('nouns.txt', 'r', encoding='utf-8') as source1:
##        s=source1.read
##        print(s)
##    return s
####        nouns=source_text.split()
####        print(nouns)
##with open('nouns.txt', 'r', encoding='utf-8') as source1:
##    s=source1.readlines
##    print(s)
##
##
##
##
####import random
####with open('words.txt', 'r', encoding='utf-8') as source:
####    lines=source.readlines()
######    line1=lines[0]
######    line2=lines[1]
######    line3=lines[2]
######    line4=lines[3]
######    line5=lines[4]
######    line6=lines[5]
####def subject():
####    subject=lines[0].split()
####    subject=random.choice(subject)
####    return subject
####subj=subject()
####def noun_phrase(subj):
####    sg_adj=lines[4].split()
####    pl_adj=lines[5].split()
####    if subj=='народ' or subj=='человек' or subj=='вирус':
####        n_ph= 'Это '  + random.choice(sg_adj) + ' ' + subj + '!'
####    else:
####        n_ph= 'Это '  + random.choice(pl_adj) + ' ' + subj + '!'
####    return n_ph
####def noun_phrase(subj):
####    sg_adj=line5.split()
####    pl_adj=line6.split()
####    if subj=='человек' or subj=='народ' or subj=='он':
####        n_ph=subj + ' ' + random.choice(sg_adj)
####    else:
####        n_ph=subj + ' ' + random.choice(pl_adj)
####    return n_ph
####def plural_subject():
####    pl_subj=line5.split()
####    return random.choice(pl_subj)
####def intransitive_predicate():
####    intrans_pred=line2.split()
####    return random.choice(intrans_pred)
####
####def transitive_predicate():
####    trans_pred=line3.split()
####    return random.choice(trans_pred)
####def proverb():
####    proverbs=line4.split(', ')
####    return random.choice(proverbs)
####def sent1():
####    return subject() + ' ' + intransitive_predicate() + ' и не ' + transitive_predicate() + ', что...' + plural_subject() + ' ' + proverb + 
####def sent2():
####    sent2 = subject() + ' ' + proverb() + ' ' + intransitive_predicate() + ' ' + ', пока ' + subject() + ' ' + intransitive_predicate() + '.'
####    return sent2.capitalize()
