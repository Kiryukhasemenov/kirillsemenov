import re
def great_changes():
    with open ('text.txt', 'r', encoding='utf-8') as source:
        old_text=source.readlines()
    for line in old_text:
        newline=re.sub(r'(\s|\(|«)динозавр((а|о|у|е|ы|»)?(м|в|х|\)|»)?и?(\s|.|,|:|;)?\s)', r'\1кот\2', line, flags=re.DOTALL)
        newline1=re.sub(r'\sДинозавр((а|о|у|е|ы)?(м|в|х)?и?(\s|.|,|:|;)?\s)', r' Кот\1', newline, flags=re.DOTALL)
        print (newline1)
    return 'That`s all!'
