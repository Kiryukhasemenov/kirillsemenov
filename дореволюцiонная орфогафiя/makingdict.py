import urllib.request
from urllib import parse
import re
import os
from bs4 import BeautifulSoup


def weather():
    req = urllib.request.Request('https://yandex.ru/pogoda/10463')
    with urllib.request.urlopen(req) as response:
        code = response.read().decode('UTF-8')
    reg=re.search('<span class="temp__value">(.*?)</span>', code, flags=re.DOTALL)
    current_weather=reg.group(1)
    return current_weather
print(current_weather())
def main_page():
    req = urllib.request.Request('https://lenta.ru/')
    with urllib.request.urlopen(req) as response:
        code = response.read().decode('UTF-8')
    soup = BeautifulSoup(code, 'html.parser')
    text = soup.get_text()
    rus=re.sub('[\s+,]',' ',text)
    rus = re.findall('[А-ЯЁа-яё ]{3,}', text)
    print(rus)
    html_clean = '\n'.join(rus)
    html_clean = re.sub('\s+', ' ', html_clean)
#    with open ('html_clean.txt', 'w', encoding='UTF-8') as file:
#        text=file.write(html_clean)
 #   os.system(r"/home/lera/ms/mystem -w -l -n " "./html_clean.txt" " ./stemmed_html.txt")
    return html_clean[:100]
print(main_page())