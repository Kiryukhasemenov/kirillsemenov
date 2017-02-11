import re
def info():
    with open ('site2.html', 'r', encoding='utf-8') as source:
        all_info=source.read()
    all_info1=re.sub(r'\s+', r' ', all_info, flags=re.DOTALL)
    table_edge=r'Семейство:.*?</td>.*?</tr>'
    table1=re.search(table_edge, all_info1)
    text=table1.group()
    word_edge=r'<a .*?>(.*)</a>'
    word1=re.search(word_edge, text)
    exact=word1.group(1)
    if table1 != None:
        with open ('family_name.txt', 'a', encoding='utf-8') as result:
            result.write(exact)
    return 'The name of the family is waiting for you in a new file.'
##def family_finder():
##    return 'nothing so far...'
##<table class="infobox".*?>.*?</table>'
##<td.*?Семейство:.*?</tr>
