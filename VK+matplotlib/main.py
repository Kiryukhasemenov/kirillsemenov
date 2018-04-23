import urllib.request
import json
offsets=[0,100,200]
for off in offsets:
    req = urllib.request.Request(
        'https://api.vk.com/method/wall.get?owner_id=-63731512&count=50&v=5.74&access_token=e710108be710108be710108b35e7723cb5ee710e710108bbdd1de6023989f2a50d061c4&offset=' + str(
            off))
    response = urllib.request.urlopen(req)
    result = response.read().decode('utf-8')
    if off == 0:
        data = json.loads(result)
    else:
        data1 = json.loads(result)
        needed_data = data1['response']['items']
        for n in needed_data:
            data['response']['items'].append(n)
#import urllib.request  # импортируем модуль
#запрос для выкачки постов
#offsets_for_posts=[0,100,200]
#totall_result=''
#for off_post in offsets_for_posts:
    #i=str(off_post//100)
#    req = urllib.request.Request('https://api.vk.com/method/wall.get?owner_id=-63731512&count=2&v=5.74&access_token=e710108be710108be710108b35e7723cb5ee710e710108bbdd1de6023989f2a50d061c4&offset='+str(off_post))
#    response = urllib.request.urlopen(req) # да, так тоже можно, не обязательно делать это с with, как в примере выше
#    result = response.read().decode('utf-8')
    #result+i=result
    #print(result)
#    totall_result=totall_result+result
#totall_result=dict(result0.items()+result1.items()+result2.items())
#print(result)
#print(totall_result)
#import json
#data = json.loads(result)
#print(type(data))

a=data['response']['items']
#print(a)
all_texts={}
text_counter=0
for a_item in a:
    text_counter=a_item['id']
    all_texts[text_counter]=[a_item['text'], len(a_item['text'].split()), a_item['comments']['count']]
#print(all_texts)

def hundreds(n):
    num=int(n)
    if num>100:
        hundreds=0
        while num>0:
            hundreds+=1
            num-=100
#            print(num)
#        print(str(num)+' '+str(hundreds))
    else:
        hundreds=1
    hundreds=[h for h in range(hundreds+1)]
    return hundreds

def make_mean_length(texts):
    #import numpy as np
    lengths=[]
    for t in texts:
        length=len(t.split())
        lengths.append(length)
    mean_length=sum(lengths)//len(lengths)
    #mean_length=np.mean(lengths)
    return mean_length

comment_info={}
id_counter=0
for text in all_texts:
#    print(all_texts[text])
    offsets = hundreds(all_texts[text][2])
    #users = set()
    comments=[]
    for off in offsets:
#        print(offsets[off])
        off=off*100
        req = urllib.request.Request('https://api.vk.com/method/wall.getComments?owner_id=-63731512&post_id='+str(text)+'&v=5.74&count=100&access_token=e710108be710108be710108b35e7723cb5ee710e710108bbdd1de6023989f2a50d061c4&offset='+str(off))
        response = urllib.request.urlopen(req) # да, так тоже можно, не обязательно делать это с with, как в примере выше
        result = response.read().decode('utf-8')
        result = json.loads(result)
#        text_info=[t for t in result['response']['items']]
#        info=
        #comment_info={}
        for t in result['response']['items']:
            id_info=t['from_id']
            comment_itself=t['text']
            lencom=len(comment_itself.split())
            comments.append(comment_itself)
            if id_info not in comment_info:
                id_counter+=1
                comment_info[id_counter]=[id_info, comment_itself, lencom]
#        for t in text_info:
#            comments.append(t['text'])
    comment_length=make_mean_length(comments)
#    print('!!!'+str(comment_length))
#    print(all_texts[text])
    all_texts[text].append(comment_length)
#    print(all_texts[text])
print(all_texts)
print(comment_info)
for_database=[]
for key in all_texts.keys():
    line=[]
    line.append(key)
    for el in all_texts[key]:
        line.append(el)
    line=tuple(line)
    for_database.append(line)
print(for_database)
#new_all=list(all_texts)
#print(new_all)


import sqlite3
conn=sqlite3.connect('vandrouki.db')
c=conn.cursor()

c.executescript('''DROP TABLE IF EXISTS posts_speakers;
CREATE TABLE IF NOT EXISTS posts_speakers (id INTEGER PRIMARY KEY AUTOINCREMENT, post_id INTEGER, post TEXT, post_length INTEGER, 
mean_comment REAL)''')
c.executemany('INSERT INTO posts_speakers VALUES (?,?,?,?,?)', for_database)
#c.execute('ALTER TABLE posts_speakers ADD COLUMN smth TEXT')
post_lengths=[]
mean_comm_lengths=[]
for raw in c.execute('''SELECT post_length, mean_comment FROM posts_speakers ORDER BY id'''):
    post_lengths.append(raw[0])
    mean_comm_lengths.append(raw[1])
print(post_lengths)
print(mean_comm_lengths)
import matplotlib.pyplot as plt
plt.scatter(post_lengths, mean_comm_lengths)
plt.xlabel('Средняя длина поста (в словах)')
plt.ylabel('Средняя длина комментария (в словах)')
#plt.show()
plt.savefig('posts_and_comments.png', format='png', dpi=100)


cities={}
birthdays={}
import pandas as pd
#df=pd.DataFrame(data=all_texts)
speakers=pd.DataFrame.from_dict(comment_info, orient='index')
speakers.head()
for speaker in speakers[0][:1000]:
    req = urllib.request.Request('https://api.vk.com/method/users.get?user_ids='+str(speaker)+'&v=5.74&fields=city,bdate&access_token=e710108be710108be710108b35e7723cb5ee710e710108bbdd1de6023989f2a50d061c4')
    response = urllib.request.urlopen(req) # да, так тоже можно, не обязательно делать это с with, как в примере выше
    result = response.read().decode('utf-8')
    result = json.loads(result)
    print(result)
    if 'response' in result:
        userdata=result['response']
        if 'bdate' not in userdata[0]:
            continue
#        birthdays[speaker]='NaN'
        birthdays[speaker]=userdata[0]['bdate']
        if 'city' not in userdata[0]:
            continue
#        cities[speaker]='NaN'
        cities[speaker]=userdata[0]['city']['title']
def age_maker(a):
    a=list(a)
    if len(a)>=8:
        byear=int(''.join(a[-4:]))
        curr_age=2018-byear
        return curr_age
    else:
        pass

for bd in birthdays:
#    bd_item=birthdays[bd]
    birthdays[bd]=age_maker(birthdays[bd])
print(birthdays)
print(cities)
c.executescript('''DROP TABLE IF EXISTS comments_speakers;
                    CREATE TABLE IF NOT EXISTS comments_speakers 
                    (speaker_id INTEGER, 
                    comment TEXT, 
                    comment_length INTEGER)''')
for comment in comment_info:
    comment_line=tuple(comment_info[comment])
    c.execute('''INSERT INTO comments_speakers VALUES (?,?,?)''', comment_line)
c.execute('''ALTER TABLE comments_speakers ADD city TEXT''')
for citied_speaker in cities:
    updater=[cities[citied_speaker], citied_speaker]
#    print(updater)
    c.execute('''UPDATE comments_speakers SET city=? WHERE speaker_id=?''', updater)
c.execute('''ALTER TABLE comments_speakers ADD age INTEGER''')
for aged_speaker in birthdays:
    updater2=[birthdays[aged_speaker],aged_speaker]
#    print(updater2)
    c.execute('''UPDATE comments_speakers SET age=? WHERE speaker_id=?''', updater2)

#def sec_db(c_i, cs, bds):
#    c.executescript('''DROP TABLE IF EXISTS comments_speakers;
#                        CREATE TABLE comments_speakers
#                        (speaker_id INTEGER,
#                        comment TEXT,
#                        comment_length INTEGER)''')
#    for comment in c_i:
#        comment_line=tuple(c_i[comment])
#        print(comment_line)
#       c.execute('''INSERT INTO comments_speakers VALUES (?,?,?)''', comment_line)
#    c.execute('''ALTER TABLE comments_speakers ADD city TEXT''')
#   for citied_speaker in cs:
#       updater=[cs[citied_speaker], citied_speaker]
#       print(updater)
#        c.execute('''UPDATE comments_speakers SET city=? WHERE speaker_id=?''', updater)
#    c.execute('''ALTER TABLE comments_speakers ADD age INTEGER''')
#    for aged_speaker in bds:
#        updater2=[bds[aged_speaker],aged_speaker]
#        print(updater2)
#        c.execute('''UPDATE comments_speakers SET age=(?) WHERE speaker_id=(?)''', updater2)
#    return 'second database done'
#sec_db(comment_info, cities, birthdays)
city_stats={}
city_stats_for_graph=[]
c.execute('''SELECT comment_length, city FROM comments_speakers WHERE city IS NOT NULL  ORDER BY speaker_id''')
raws = c.fetchall()
for raw in raws:
    print(raw)
    if raw[1] not in city_stats:
        city_stats[raw[1]]=[0]
        city_stats[raw[1]].append(raw[0])
        print(city_stats)
        print('ok', city_stats[raw[1]])
    else:
        print('crash', city_stats[raw[1]])
        city_stats[raw[1]].append(raw[0])
for city in city_stats:
        #city_stats[city]=np.array(city_stats[city])
        #city_stats[city]=(city_stats[city])
    print(city_stats[city])
    city_stats[city]=(sum(city_stats[city])/len(city_stats[city]))
    #city_stats_for_graph.append(city_stats[city])

print(post_lengths)
print(mean_comm_lengths)
#import matplotlib.pyplot as plt
plt.clf()
plt.bar(city_stats.keys(), city_stats.values())
plt.xlabel('Город')
plt.xticks(range(len(city_stats.keys())), city_stats.keys(), rotation=90)
plt.ylabel('Средняя длина комментария (в словах)')
#plt.show()
plt.savefig('cities_and_comments.png', format='png', dpi=100)

age_stats={}
age_stats_for_graph=[]
for raw in c.execute('''SELECT comment_length, age FROM comments_speakers WHERE age IS NOT NULL ORDER BY speaker_id'''):
    if raw[1] not in age_stats:
        #age_stats[raw[1]]=[]
        age_stats[raw[1]]=[raw[0]]
    else:
        age_stats[raw[1]].append(raw[0])
for age1 in age_stats:
        #age_stats[age1]=np.mean(age_stats[age1])
    #age_stats_for_graph.append(age_stats[age1])
    age_stats[age1]=sum(age_stats[age1])/len(age_stats[age1])
print(age_stats)
plt.clf()
plt.scatter(age_stats.keys(), age_stats.values())
plt.xlabel('Возраст')
plt.ylabel('Средняя длина комментария (в словах)')
#plt.show()
plt.savefig('age_and_comments.png', format='png', dpi=100)
		
conn.commit()


