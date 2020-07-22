Python 3.7.0a1 (v3.7.0a1:8f51bb4, Sep 19 2017, 19:32:44) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> '''
1. Достукиваем до текста( description)
2. Создаем список из слов путем split(' ')
3. Удаляем из списка те слова, что менее 6 букв.
4. Через count запоминаем кол-во повторений слов.
5. Создаем новый список. Через Counter most_common.
'''


import json


with open('newsafr.json', encoding='utf-8') as f:
   json_data = json.load(f)
description = json_data['rss']['channel']['items']
des = [i['description'] for i in description]
a_list = [de.split(' ') for de in des] 
lower_list = [s.lower() for a in a_list for s in a]
words_longer_6 = []
for word in lower_list:
    if len(word) >= 6:
      words_longer_6.append(word)

from collections import Counter
top_words = Counter(words_longer_6).most_common(10)
for readble in top_words:
  print(readble)







import xml.etree.ElementTree as ET
tree = ET.parse('Homework8-XML.xml')
root = tree.getroot()
des = root.findall('channel/item/description')
news_list = [readble.text for readble in des] 

a_list = [de.split(' ') for de in news_list] 
lower_list = [s.lower() for a in a_list for s in a]
words_longer_6 = []
for word in lower_list:
    if len(word) >= 6:
      words_longer_6.append(word)

from collections import Counter
top_words = Counter(words_longer_6).most_common(10)
for readble in top_words:
  print(readble)
