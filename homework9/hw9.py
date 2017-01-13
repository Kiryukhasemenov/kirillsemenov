def opener(text):
    with open(text, 'r', encoding='utf-8') as source:
        whole_text=source.read()
    words=whole_text.split()
    number_of_adj=int()
    lengths=int()
    adj=[]
    for i in range(len(words)):
        word=words[i]
        word=word.strip('.,`?!()”')
        if word.endswith('ous'):
            number_of_adj+=1
            adj.append(word)
            length_of_word=len(word)
            lengths+=length_of_word
    print('Number of words ending with "-ous" equals ', str(number_of_adj))
    print('Average length of word is: ', str(round(lengths/number_of_adj)))
    return 'Program complete'

def name():
    n=input('Put the name of the file in: ')
    return opener(n)
