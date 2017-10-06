import urllib.request
import re
import os
import time
def dirmak():
    types=['plain', 'mystem-xml', 'mystem-plain']
    years=['2016', '2015', '2014', '2013', '2012']
    months=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
    for t in types:
        tdir='.\\'+str(t)
        os.mkdir(tdir)
#        print(tdir)
        for y in years:
            ydir=tdir+'\\'+str(y)
            os.mkdir(ydir)
 #           print(ydir)
            for m in months:
                mdir=ydir+'\\'+str(m)
                os.mkdir(mdir)
#                print(mdir)
#dirmak()

def crwlr():
    base='http://old.gazetayakutia.ru/index.php/archive/item/'
    all_arts=[]
    for i in range(23040,23240):
        each_art=base+str(i)

        try:
            req = urllib.request.Request(str(each_art))
            with urllib.request.urlopen(req) as source:
                html=source.read().decode('utf-8')

            all_arts.append(each_art)
        except:
            pass
    return all_arts

def f1(s):
    wordNum=int()
#    time.sleep(5)
    for site in s:
#        print(site)
        siteNumber=re.search('item/(.*)', site, flags=re.DOTALL)
        siteNumber=siteNumber.group(1)
        print(siteNumber)
        req = urllib.request.Request(str(site))
        with urllib.request.urlopen(req) as source:
            html=source.read().decode('utf-8')

        name=f6(html)
        dat=f2(html)
        topic=f3(html)
        year=dat[-4:]
        url=f4(html)
        author=f5(html)
        regTag = re.compile('<.*?>', re.DOTALL)  
        regScript = re.compile('<script.*?>.*?</script>', re.DOTALL) 
        regComment = re.compile('<!--.*?-->', re.DOTALL) 
        regSpace = re.compile('\s{2,}', re.DOTALL)
        regLatinToTheHell=re.compile('[a-zA-Z0-9_#;&/\№|=\{\}]', re.DOTALL)
        regPunctToTheHell=re.compile(' [:\."\?\(\)\-;,]{2} ', re.DOTALL)
        regPunctToTheHell2=re.compile(' [:\."\?\(\)\-;,] ', re.DOTALL)
        clean_t = regScript.sub(" ", html)
        clean_t = regComment.sub(" ", clean_t)
        clean_t = regTag.sub(" ", clean_t)
        
        clean_t=regLatinToTheHell.sub(" ", clean_t)
        clean_t=regPunctToTheHell.sub(" ", clean_t)
        clean_t=regPunctToTheHell2.sub(" ", clean_t)
        clean_t = regSpace.sub (" ", clean_t)
        wordNum+=len(clean_t.split(' '))
        date=dat.split('.')
        date=''.join(date)
        fileName=siteNumber+'-'+str(date)
        neededPath=f7(fileName)
 #       print(neededPath)

        row = '%s\t%s\t\t\t%s\t%s\tпублицистика\t\t\t%s\t\tнейтральный\tн-возраст\tн-уровень\tреспубликанская\t%s\tгазета "Якутия"\t\t%s\tгазета\tРоссия\tЯкутия\tru'
        meta=str(row%(neededPath,author,name,dat,topic,url,year))

        with open(neededPath, 'w', encoding='utf-8') as article:
            article.write('@au '+author+'\n')
            article.write('@ti '+name+'\n')
            article.write('@da '+dat+'\n')
            article.write('@topic '+topic+'\n')
            article.write('@url '+url+'\n')
            article.write(clean_t)
        pathForMystem1=re.sub('plain','mystem-xml', neededPath, flags=re.DOTALL)
        with open (pathForMystem1, 'w', encoding='utf-8') as mstmarticle1:
            mstmarticle1.write(clean_t)
        mstm1(pathForMystem1)    
        pathForMystem2=re.sub('plain','mystem-plain', neededPath, flags=re.DOTALL)
        with open (pathForMystem2, 'w', encoding='utf-8') as mstmarticle2:
            mstmarticle2.write(clean_t)
        mstm2(pathForMystem2)
#        print('something with txt done')
        print('something with xml is done')
        with open('metadata.csv', 'a', encoding='utf-8') as metadata:
            metadata.write(meta+'\n')
        time.sleep(3)
    print('see ya! the number of words is: '+str(wordNum))
    return 'see ya! the number of words is: '+str(wordNum)+'!!!'
        
def f6(text):
    name_part=re.search('<meta name="title" content="(.*?)" />', text, flags=re.DOTALL)
    clean_name=name_part.group(1)
    return clean_name
def f2(text):
    date_part=re.search('<!-- Date created -->(.*?)</li>', text, flags=re.DOTALL)
    all_date=(date_part.group(1)).split(' ')

    months={'January':'01', 'February':'02', 'March':'03', 'April':'04', 'May':'05', 'June':'06', 'July':'07', 'August':'08', 'September':'09', 'October':'10', 'November':'11', 'December':'12'}
    needed_date=str(all_date[1]+'.'+months[all_date[2]]+'.'+all_date[3])
    return needed_date
def f3(text):
    topic_part=re.search('class="itemTags">.*?<li><a href=".*?">(.*?)</a></li>', text, flags=re.DOTALL)
    if topic_part != None:
        
        needed_topic=topic_part.group(1)
        return needed_topic
    else:
        return 'no topic'

def f4(text):
    url_part=re.search('<base href="(.*?)" />', text, flags=re.DOTALL)
    needed_url=url_part.group(1)
    return needed_url

def f5(text):
    auth_part=re.search('K2_WRITTEN_BY.*?(([а-яА-Я]+ [а-яА-Я]+)|(maxim)).*?</.*?>', text, flags=re.DOTALL)
    potential_auth=auth_part.group(1)
    if potential_auth=='maxim':
        return 'Noname'
    else:
        return potential_auth

def f7(n):
    year_v=n[-4:]
    month_v=n[-6:-4]
#    print('!' + str(month_v))
    if month_v[0]=='0':
        month_v=str(month_v)[1]
#        print('change '+str(month_v))
    ult_path='.\\plain\\'+str(year_v)+'\\'+str(month_v)+'\\'+str(n)+'.txt'
    return ult_path

def mstm1(p):
    futurexml=re.sub('\.txt', 'new', p, flags=re.DOTALL)
    os.system('C:\\Users\\lenovo\\Desktop\\mystem.exe -nid --format xml '+p+' '+futurexml)
    os.remove(p)
    return 'xml done'

def mstm2(p):
    future=re.sub('\.txt', 'new', p, flags=re.DOTALL)
    os.system('C:\\Users\\lenovo\\Desktop\\mystem.exe -nid '+p+' '+future)
    os.remove(p)
    return 'plain mystem done'
    

f1(crwlr())
