all_words=[]
new_element=input()
while new_element:
    word=list(new_element)
    if word[-1]=="r" and word[-2]=="u" and word[-3]=="t":
        good_word="".join(word)
        all_words.append(good_word)
    new_element=input()
for i in range(len(all_words)):
    print(all_words[i])
    
