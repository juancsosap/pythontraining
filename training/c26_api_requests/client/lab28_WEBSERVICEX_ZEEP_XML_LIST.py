#!/usr/bin/env python
# encoding: utf-8

import xml.etree.ElementTree as et
from zeep import Client
# pip install zeep


book = 'John'
chapter = 7

client = Client('http://www.webservicex.net/BibleWebservice.asmx?WSDL')
result = client.service.GetBibleWordsByBookTitleAndChapter(book, chapter)

xml_response = et.fromstring(result)

verses = xml_response.findall('.//Table')

for verse in verses:
    number = verse.find('Verse').text
    text = verse.find('BibleWords').text
    print('{} {}:{}\t{}'.format(book, chapter, number, text))
