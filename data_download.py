def print_hi(name):
    print(f'Hi, {name}')

if __name__ == '__main__':
    print_hi('PyCharm')

import requests
from bs4 import BeautifulSoup as bs4
from collections import defaultdict
from tqdm import tqdm
import os



def get_links(link):

    page = requests.get(link)
    bss = bs4(page.content, "html.parser")
    imgs = bss.find_all("img")
    imgs = imgs[3:-1]
    jpegs = []

    for img in imgs:

        imglink = img.attrs.get("data-src")
        imglink = str(imglink)

        if imglink.endswith("jpg"):

            jpegs.append(imglink)

    return jpegs


search_links_dict_train = {
    'tesettur_urls' : 'https://www.ciceksepeti.com/moda?c=15030&df=2006847,2006848&page=',
    'kazak_urls' : 'https://www.trendyol.com/sr?q=kazak&qt=kazak&st=kazak&os=1&pi=',
    'gomlek_urls' : 'https://www.ciceksepeti.com/moda?c=14950&df=2006847,2006848&page=',
    'mont_urls' : 'https://www.ciceksepeti.com/moda?c=14954&df=2006847,2006848&page=',
    'dress_urls' : 'https://www.ciceksepeti.com/arama?query=elbise&qt=elbise&choice=1&page=',
    'gecelik_urls' : 'https://www.ciceksepeti.com/moda?c=14916&df=2006847,2006848&page=',
    'sort_urls': 'https://www.ciceksepeti.com/moda?c=14908&df=2006847,2006848&page=',
    'tayt_urls':  'https://www.ciceksepeti.com/moda?c=14909&df=2006847,2006848&page=',
    't_shirt_urls' : 'https://www.ciceksepeti.com/arama?query=t-shirt&qt=t-shirt&choice=2&page=',
    'panth_urls' :'https://www.ciceksepeti.com/arama?query=pantolon&qt=pantolon&choice=1&page=',

}

urls_dict = defaultdict(list)

for k,v in search_links_dict_train.items():
    for i in range(2,18):
        urls_dict[f'{k}_search'].append(f'{v}{i}')

item2jpg = defaultdict(list)

for key, links in urls_dict.items():
    for link in links:

        item2jpg[key] += get_links(link)
    print('-----------------------------------------')
    #print(item2jpg[key])
    #print(len(item2jpg[key]))

num = 1

for name in item2jpg.keys():
    dir = os.path.join(r"/Users/mertsengil/Desktop/datas2/data/train", f'{name}_train')
    if not os.path.exists(dir):
        os.mkdir(dir)

    file1 = os.chdir(dir)
    for jpg in tqdm(item2jpg[name]):

        myfile = str(num) + '.jpg'
        file1 = open(myfile, "wb")

        jpgx = requests.get(jpg).content
        file1.write(jpgx)
        num += 1

search_links_dict_test = {
    'tesettur_urls': 'https://www.ciceksepeti.com/moda?c=15030&df=2006847,2006848&page=',
    'kazak_urls': 'https://www.ciceksepeti.com/moda?c=14953&df=2006847,2006848&page=',
    'gomlek_urls': 'https://www.ciceksepeti.com/moda?c=14950&df=2006847,2006848&page=',
    'mont_urls': 'https://www.ciceksepeti.com/moda?c=14954&df=2006847,2006848&page=',
    'dress_urls': 'https://www.ciceksepeti.com/arama?query=elbise&qt=elbise&choice=1&page=',
    'gecelik_urls': 'https://www.ciceksepeti.com/moda?c=14916&df=2006847,2006848&page=',
    'sort_urls': 'https://www.ciceksepeti.com/moda?c=14908&df=2006847,2006848&page=',
    'tayt_urls': 'https://www.ciceksepeti.com/moda?c=14909&df=2006847,2006848&page=',
    't_shirt_urls': 'https://www.ciceksepeti.com/arama?query=t-shirt&qt=t-shirt&choice=2&page=',
    'panth_urls': 'https://www.ciceksepeti.com/arama?query=pantolon&qt=pantolon&choice=1&page=',

    }

urls_dict = defaultdict(list)

for k, v in search_links_dict_test.items():
    for i in range(19, 23):
        urls_dict[f'{k}_search'].append(f'{v}{i}')

item2jpg = defaultdict(list)
for key, links in urls_dict.items():
    for link in links:
        item2jpg[key] += get_links(link)
    print('-----------------------------------------')
        # print(item2jpg[key])
        # print(len(item2jpg[key]))

for name in item2jpg.keys():
    dir = os.path.join(r"/Users/mertsengil/Desktop/datas2/data/test", f'{name}_test')
    if not os.path.exists(dir):
        os.mkdir(dir)

    file1 = os.chdir(dir)
    for jpg in tqdm(item2jpg[name]):
        myfile = str(num) + '.jpg'

        file1 = open(myfile, "wb")

        jpgx = requests.get(jpg).content
        file1.write(jpgx)
        num += 1