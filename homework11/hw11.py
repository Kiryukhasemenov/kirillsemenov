import re
def word_form_finder():
    with open ('text.txt', 'r', encoding='utf-8') as source:
        text=source.read()
        tokens=text.split()
        bare_tokens=[]
        for i in range(len(tokens)):
            token=tokens[i]
            token=token.strip('.,!?")')
            bare_tokens.append(token)
    eat_forms="(С|с)ъе(м|ш|с|д|л|в)(ь|т|и|я|а|о|ш)?(м|т|и)?(е|и)?"
    for i in range(len(bare_tokens)):
        result=re.search(eat_forms,bare_tokens[i])
        if result != None:
            print (bare_tokens[i])
    return 'Вот все словоформы слова "съесть".'
