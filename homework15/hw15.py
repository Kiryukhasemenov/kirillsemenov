import os
import re
def f():
    all_files=os.listdir('.')
    needed=[]
    file_name='.*\.\w\w(\w)?'
    for i in range(len(all_files)):
        item=all_files[i]
        result=re.search(file_name, item)
        if result == None:
            needed.append(item)

    return needed
def f2(s):
    fin=[]
    for f in range(len(s)):
        fold=s[f]
        words=fold.split()
        numwords=len(words)
        if numwords > 1:
            fin.append(fold)        
    return fin

f2(f())
