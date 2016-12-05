with open("text.txt", "r", encoding="utf-8") as f:
    old_text=f.read()
    text=old_text.replace('.', '')
    text=text.replace(',', '')
    words=text.split(' ')
    number=int()
    for i in range(len(words)):
        if len(words[i])>10:
            number+=1
    percent=(number/len(words))*100
    print("Процент слов, содержащих более 10 символов: ", round(percent))
