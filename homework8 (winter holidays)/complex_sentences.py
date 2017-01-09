##1 - сложносочиненное предложение с разделительными союзами - done
##2 - сложноподчиненное с придаточным изъяснительным - done, although not perfectly...
##3 - сложноподчиненное с придаточным времени - done
#4 - бессоюзное сложное предложение - done
##5 - многоуровневое сложносочиненное+сложноподчиненное+бессоюзное - done
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
    with open('transitive_verbs.txt', 'r', encoding='utf-8') as source2_1:
##        line=source2.read()
##        tr_verbs=line.split()
        lines=source2_1.readlines()
        verbs_sg=lines[0].split()
        verbs_pl=lines[1].split()
    with open('nouns_acc.txt', 'r', encoding='utf-8') as source2_2:
        objects=source2_2.read()
        objects=objects.split()
    if subj[-1]=='и' or subj[-1]=='ы':
        return subj + ' ' + random.choice(verbs_pl) + ' ' + random.choice(objects)
    else:
        return subj + ' ' + random.choice(verbs_sg) + ' ' + random.choice(objects)
##    tr_verb=random.choice(tr_verbs)
##    return tr_verb
def noun_phrase(subj):
    with open('adjectives.txt', 'r', encoding='utf-8') as source3:
        lines=source3.readlines()
        m_adj=lines[0].split()
        f_adj=lines[1].split()
        pl_adj=lines[2].split()
        n_adj=lines[3].split()
    if subj[-1]=='а' or subj[-1]=='я' or subj[-1]=='ь':
        return random.choice(f_adj) + ' ' + subj
    elif subj[-1]=='и' or subj[-1]=='ы':
        return random.choice(pl_adj) + ' ' + subj
    elif subj[-1]=='о' or subj[-1]=='е':
        return  random.choice(n_adj) + ' ' + subj
    else:
        return random.choice(m_adj) + ' ' + subj
def adverb():
    with open('adverbs.txt', 'r', encoding='utf-8') as source4:
        line=source4.read()
        advs=line.split(', ')
    return random.choice(advs)
def intransitive_verb(subj):
    with open('intransitive_verbs.txt', 'r', encoding='utf-8') as source5:
##        line=source5.read()
##        intr_verbs=line.split()
        lines=source5.readlines()
        verbs_sg=lines[0].split()
        verbs_pl=lines[1].split()
    if subj[-1]=='и' or subj[-1]=='ы':
        return subj + ' ' + random.choice(verbs_pl)
    else:
        return subj + ' ' + random.choice(verbs_sg)
def bare_intransitive_verb(subj):
    with open('intransitive_verbs.txt', 'r', encoding='utf-8') as source5:
        lines=source5.readlines()
        verbs_sg=lines[0].split()
        verbs_pl=lines[1].split()
    if subj[-1]=='и' or subj[-1]=='ы':
        return random.choice(verbs_pl)
    else:
        return random.choice(verbs_sg)
##
##
##    if subj=='они':
##        return random.choice(verbs_pl)
##    elif subj=='он' or subj=='она' or subj=='оно':
##        return random.choice(verbs_sg)
def past_tense_clause(subj):
    with open('verbs-praet.txt', 'r', encoding='utf-8') as source6_1:
        lines=source6_1.readlines()
        verbs_m=lines[0].split(', ')
        verbs_f=lines[1].split(', ')
        verbs_pl=lines[2].split(', ')
        verbs_n=lines[3].split(', ')
    with open ('conjunctions.txt', 'r', encoding='utf-8') as source7:
        conjs=source7.readlines()
        time_conjs=conjs[2].split(', ')
        conj=random.choice(time_conjs)
    if subj[-1]=='и' or subj[-1]=='ы':
        return conj + ' ' + subj + ' ' + random.choice(verbs_pl)    
    elif subj[-1]=='а' or subj[-1]=='я' or subj[-1]=='ь':
        return conj + ' ' + subj + ' ' + random.choice(verbs_f)
    elif subj[-1]=='о' or subj[-1]=='е':
        return conj + ' ' + subj + ' ' + random.choice(verbs_n)
    else:
        return conj + ' ' + subj + ' ' + random.choice(verbs_m)
def conjunction(v):
    with open ('conjunctions.txt', 'r', encoding='utf-8') as source7:
        conjs=source7.readlines()
        corr_conjs=conjs[0].split(', ')
        expr_conjs=conjs[1].split(', ')
    if v==expressing_verb(subject()):
        conj=random.choice(expr_conjs)
        if conj=='как' or conj=='насколько':
            return conj + ' ' + adverb() + ' '
        else:
            return conj + ' '
    else:
        return random.choice(corr_conjs) + ' '
def expr_conjunction():
    with open ('conjunctions.txt', 'r', encoding='utf-8') as source7:
        conjs=source7.readlines()
        expr_conjs=conjs[1].split(', ')
    conj=random.choice(expr_conjs)
    if conj=='как' or conj=='насколько':
        return conj + ' ' + adverb() + ' '
    else:
        return conj + ' '
def time_conjunction():
    with open ('conjunctions.txt', 'r', encoding='utf-8') as source7:
        conjs=source7.readlines()
        time_conjs=conjs[2].split(', ')
    conj=random.choice(time_conjs)
    return conj + ' '
def expressing_verb(subj):
    with open('verbs-for-clauses.txt', 'r', encoding='utf-8') as source8:
        lines=source8.readlines()
        verbs_sg=lines[0].split()
        verbs_pl=lines[1].split()
    if subj[-1]=='и' or subj[-1]=='ы':
        return random.choice(verbs_pl)
    else:
        return random.choice(verbs_sg)
def verb_of_sence(subj):
   with open('verbs-of-sences.txt', 'r', encoding='utf-8') as source9:
        lines=source9.readlines()
        verbs_m=lines[0].split()
        verbs_f=lines[1].split()
        verbs_pl=lines[2].split()
        verbs_n=lines[3].split()
   if subj[-1]=='и' or subj[-1]=='ы':
       return random.choice(verbs_pl)    
   elif subj[-1]=='а' or subj[-1]=='я' or subj[-1]=='ь':
       return random.choice(verbs_f)
   elif subj[-1]=='о' or subj[-1]=='е':
       return random.choice(verbs_n)
   else:
       return random.choice(verbs_m)

def pronoun(subj):
    if subj[-1]=='и' or subj[-1]=='ы':
        return 'они '
    elif subj[-1]=='а' or subj[-1]=='я':
        return 'она '
    elif subj[-1]=='о' or subj[-1]=='е':
        return 'оно '
    else:
        return 'он '
def nominal_sentence(subj):
    with open('adjectives.txt', 'r', encoding='utf-8') as source3:
        lines=source3.readlines()
        m_adj=lines[0].split()
        f_adj=lines[1].split()
        pl_adj=lines[2].split()
    if subj[-1]=='и' or subj[-1]=='ы':
        return subj + ' - ' + random.choice(pl_adj)
    elif subj[-1]=='а' or subj[-1]=='я' or subj[-1]=='ь':
        return subj + ' - ' + random.choice(f_adj)
    elif subj[-1]=='о' or subj[-1]=='е':
        return subj + ' - ' + random.choice(n_adj)
    else:
        return subj + ' - ' + random.choice(m_adj)
def modal_word():
    with open('modal_words.txt', 'r', encoding='utf-8') as source3:
        words=source3.read()
        m_w=words.split()
    return random.choice(m_w)
##def pronoun(acc):
##    if 'его' in acc or 'человека' in acc:
##        return 'он'
##    elif acc=='армию' or acc=='жену' or acc=='ванную':
##        return 'она'
##    elif acc=='окно':
##        return 'оно'
##    else:
##        return 'они'







##тут буду писать предложения:
def sent1():
    conj=conjunction(intransitive_verb(subject()))
    sent=conj + adverb() + ' ' + intransitive_verb(subject()) + ', ' + conj + transitive_verb(noun_phrase(subject())) + '...'
    return sent.capitalize()
def sent2():
    s=subject()
    sent=s + ' ' + expressing_verb(s) + ', ' + expr_conjunction() + intransitive_verb(subject()) + '.'
    return sent.capitalize()
def sent3():
    s=subject()
    sent=past_tense_clause(s) + ', ' + pronoun(s) + modal_word()+ ' ' + adverb() + ' ' + bare_intransitive_verb(s) + '.'
    return sent.capitalize()
def sent4():
    s=subject() 
    sent=s + ' ' + verb_of_sence(s)+ ': ' + intransitive_verb(subject()) + ', ' + intransitive_verb(noun_phrase(subject())) + ', ' + adverb() + ' ' + intransitive_verb(subject()) + '...'
    return sent.capitalize()
def sent5():
    s1=subject()
    s2=noun_phrase(subject())
    sent=past_tense_clause(s1) + ', ' + pronoun(s1) + modal_word() + ' ' + bare_intransitive_verb(s1) + ', a ' + transitive_verb(s2) + ' и ' + expressing_verb(s2) + ': ' + nominal_sentence(subject()) + '.'
    return sent.capitalize()
##def sent2():
##    main_clause=transitive_verb(subject())
##    words=main_clause.split()
##    if words[-1]=='его' or words[-1]=='человека':
##        sentence=main_clause + ', пока ' + intransitive_verb('он') + '.' 
##    elif words[-1]=='армию' or words[-1]=='жену' or words[-1]=='ванную':
##        sentence=main_clause + ', пока ' + intransitive_verb('она') + '.'
##    elif words[-1]=='окно':
##        sentence=main_clause + ', пока ' + intransitive_verb('оно') + '.'
##    else:
##        sentence=main_clause + ', пока ' + intransitive_verb('они') + '.'
##    return sentence.capitalize()
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




## тут финальная моя функция будет:


def sequence_of_sentences():
    print('1. ', sent1())
    print('2. ', sent2())
    print('3. ', sent3())
    print('4. ', sent4())
    print('5. ', sent5())
    return 'Внимание! разделение на грамматические категории сделано в соответствии со "школьной" грамматикой и не будет работать с такими исключениями. как "путь", несклоняемыми существительными и т.д. Прошу прощения...'
