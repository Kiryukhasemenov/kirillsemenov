##обходить всё дерево папок, начинающееся с той папки, где она находится, и сообщать следующую информацию
##сколько в этих папках встречается разных названий файлов без учёта расширений;
import os
import re
def f1():
    massgrave=[]
    file_type='.*\.\w\w(\w)?'
    for root, dirs, files in os.walk('.'):
        for file in files:
            file_name=re.sub(r'(.*)\.\w\w(\w)?(\w)?', r'\1', file, flags=re.DOTALL)
            print(file + ' - '+ file_name)
            if file_name not in massgrave:
                massgrave.append(file_name)
    return massgrave
f1()
