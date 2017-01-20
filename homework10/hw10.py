import random
def bigram_hints():
    bigram={}
    with open('bigrams.csv', 'r', encoding='utf-8') as source:
        lines=source.readlines()
        nouns=[]
        for line in lines:
            words=line.split(', ')
            noun=words[0]
            nouns.append(noun)
            adjs=[]
            for i,word in enumerate(words):
                if i>0:
                    adjs.append(word)
            bigram[noun]=adjs
      
    print('Поиграем в "угадай слово"!')
    task_noun=random.choice(nouns)
    word=str()
    for i in range(len(bigram[task_noun])):
        hint=bigram[task_noun][i]
        print('Попытка №' +str(i+1) + '. Подсказка: ' + hint)
        word=input('Угадай существительное: ')
        if word==task_noun:
            return 'правильно! ты угадал с попытки №' + str(i+1)
        else:
            print('Неправильно. Попытка №' + str(i+1) + ' не удалась.')
    return 'Увы, ты не угадал и проиграл('
##    while word!='война':
##        for i in range(len(bigram['война'])):
##            hint=bigram['война'][i]
##            print('Подсказка: ' + hint)
##            word=input('Угадай существительное: ')
##        print('неправильно, го еще ')
##    return 'правильно!'
