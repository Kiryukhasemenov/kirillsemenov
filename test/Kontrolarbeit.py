f=open('freq.txt', 'r', encoding='utf-8')
lines=f.readlines()
for i in range(len(lines)):
    word_charact=lines[i].split(' | ')
    if word_charact[1]=='союз':
        print(lines[i])
print("Кажется, первое задание выполнено. Перейдем ко второму:")
femine_nouns=[]
ipm_sum=int()
for i in range(len(lines)):
    word_charact=lines[i].split(' | ')
    word_charact2=word_charact[1].split(' ')
    if word_charact2[0]=="сущ"  and word_charact2[2]=="ед" and word_charact2[3]=="жен":
        print(word_charact[0])
        femine_nouns.append(word_charact[0])
        number=int(word_charact[2])
        ipm_sum+=number
text=", ".join(femine_nouns)
print(text)
print(ipm_sum)
f.close()
        
## and word_charact2[2]=="ед" and word_charact2[3]=="жен"
