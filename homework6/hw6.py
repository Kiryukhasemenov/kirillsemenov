word=input("Введите слово: ")
wordlist=list(word)
table=[]

for i in range(len(wordlist)):
    table.append(wordlist[i:])
new_table=table[::-1]
for a in range(len(new_table)):
    print("".join(new_table[a]))
    
