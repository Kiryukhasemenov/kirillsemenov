##план работы:
##1 - сложносочиненное предложение с разделительными союзами - done
##2 - сложноподчиненное с придаточным изъяснительным - done, although not perfectly...
##3 - сложноподчиненное с придаточным времени - done
##4 - бессоюзное сложное предложение - done
##5 - многоуровневое сложносочиненное+сложноподчиненное+бессоюзное - done


## здесь собраны функции-элементы предложений
import random
def subject():
    with open('nouns.txt', 'r', encoding='utf-8') as source1:
        lines=source1.read()
        nouns=lines.split()
    subject=random.choice(nouns)
    return subject
def transitive_verb(subj):
    with open('transitive_verbs.txt', 'r', encoding='utf-8') as source2_1:
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
        lines=source5.readlines()
        verbs_sg=lines[0].split()
        verbs_pl=lines[1].split()
    if subj[-1]=='и' or subj[-1]=='ы':
        return subj + ' ' + random.choice(verbs_pl)
    else:
        return subj + ' ' + random.choice(verbs_sg)
def bare_intransitive_verb(subj):
    with open('intransitive_verbs.txt', 'r', encoding='utf-8') as source6:
        lines=source6.readlines()
        verbs_sg=lines[0].split()
        verbs_pl=lines[1].split()
    if subj[-1]=='и' or subj[-1]=='ы':
        return random.choice(verbs_pl)
    else:
        return random.choice(verbs_sg)
def past_tense_clause(subj):
    with open('verbs-praet.txt', 'r', encoding='utf-8') as source7_1:
        lines=source7_1.readlines()
        verbs_m=lines[0].split(', ')
        verbs_f=lines[1].split(', ')
        verbs_pl=lines[2].split(', ')
        verbs_n=lines[3].split(', ')
    with open ('conjunctions.txt', 'r', encoding='utf-8') as source7_2:
        conjs=source7_2.readlines()
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
    with open ('conjunctions.txt', 'r', encoding='utf-8') as source8:
        conjs=source8.readlines()
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
    with open ('conjunctions.txt', 'r', encoding='utf-8') as source9:
        conjs=source9.readlines()
        expr_conjs=conjs[1].split(', ')
    conj=random.choice(expr_conjs)
    if conj=='как' or conj=='насколько':
        return conj + ' ' + adverb() + ' '
    else:
        return conj + ' '
def time_conjunction():
    with open ('conjunctions.txt', 'r', encoding='utf-8') as source10:
        conjs=source10.readlines()
        time_conjs=conjs[2].split(', ')
    conj=random.choice(time_conjs)
    return conj + ' '
def expressing_verb(subj):
    with open('verbs-for-clauses.txt', 'r', encoding='utf-8') as source11:
        lines=source11.readlines()
        verbs_sg=lines[0].split()
        verbs_pl=lines[1].split()
    if subj[-1]=='и' or subj[-1]=='ы':
        return random.choice(verbs_pl)
    else:
        return random.choice(verbs_sg)
def verb_of_sence(subj):
   with open('verbs-of-sences.txt', 'r', encoding='utf-8') as source12:
        lines=source12.readlines()
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
    with open('adjectives.txt', 'r', encoding='utf-8') as source13:
        lines=source13.readlines()
        m_adj=lines[0].split()
        f_adj=lines[1].split()
        pl_adj=lines[2].split()
        n_adj=lines[3].split()
    if subj[-1]=='и' or subj[-1]=='ы':
        return subj + ' - ' + random.choice(pl_adj)
    elif subj[-1]=='а' or subj[-1]=='я' or subj[-1]=='ь':
        return subj + ' - ' + random.choice(f_adj)
    elif subj[-1]=='о' or subj[-1]=='е':
        return subj + ' - ' + random.choice(n_adj)
    else:
        return subj + ' - ' + random.choice(m_adj)
def modal_word():
    with open('modal_words.txt', 'r', encoding='utf-8') as source14:
        words=source14.read()
        m_w=words.split()
    return random.choice(m_w)

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


## тут финальная моя функция будет:

def sequence_of_sentences():
    print('1. ', sent1())
    print('2. ', sent2())
    print('3. ', sent3())
    print('4. ', sent4())
    print('5. ', sent5())
    return 'Внимание! разделение на грамматические категории сделано в соответствии со "школьной" грамматикой и не будет работать с такими исключениями, как "путь", несклоняемыми существительными и т.д. Прошу прощения...'
