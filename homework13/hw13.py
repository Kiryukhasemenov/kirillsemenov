import re
def change():
    with open ('text.txt', 'r', encoding='utf-8') as source:
        old_text=source.readlines()
    with open ('newtext.txt', 'w', encoding='utf-8') as blocknote:
        for line in old_text:
            newline=re.sub(r'(\s|\(|«)?динозавр((а|о|у|е|ы)?(м|в|х)?и?(\s|.|,|:|;)?(\[|\s|\)|»))', r'\1кот\2', line, flags=re.DOTALL)
            newline1=re.sub(r'(\s|\(|«)?Динозавр((а|о|у|е|ы)?(м|в|х)?и?(\s|.|,|:|;)?(\[|\s|»))', r'\1Кот\2', newline, flags=re.DOTALL)
            blocknote.write(newline1)
    return 'That`s all!'

change()
