# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from urllib2 import urlopen
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#Адрес страницы
HTML_ADDRESS = "http://auto.mail.ru/catalog/"
 
html_doc = urlopen(HTML_ADDRESS, context=ctx).read()

soup = BeautifulSoup(html_doc)
 
for link in soup.find_all("div", {"class":"cols__wrapper"}):
    print link.contents[0]
#print soup