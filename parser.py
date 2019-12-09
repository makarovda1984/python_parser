# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from urllib2 import urlopen

#Адрес страницы
HTML_ADDRESS = "http://auto.mail.ru/catalog/"
 
html_doc = urlopen(HTML_ADDRESS).read()

soup = BeautifulSoup(html_doc)
 
for link in soup.find_all("div", {"class":"cols__wrapper"}):
    print link.contents[0]
#print soup