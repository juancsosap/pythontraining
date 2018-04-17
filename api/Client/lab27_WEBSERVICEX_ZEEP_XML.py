#!/usr/bin/env python
# encoding: utf-8

import xml.etree.ElementTree as et
from zeep import Client
# pip install zeep


book = 'John'
chapter = 1
verse = 1

client = Client('http://www.webservicex.net/BibleWebservice.asmx?WSDL')
result = client.service.GetBibleWordsByChapterAndVerse(book, chapter, verse)

xml_response = et.fromstring(result)

text = xml_response.find('.//BibleWords').text
ref = '{} {}:{}'.format(book, chapter, verse)
print(ref, text)
