#!/usr/bin/env python
# encoding: utf-8

import requests
import xml.etree.ElementTree as et

book = 'John'
chapter = 1
verse = 1

request = '''
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:web="http://www.webserviceX.NET">
   <soapenv:Header/>
   <soapenv:Body>
      <web:GetBibleWordsByChapterAndVerse>
         <!--Optional:-->
         <web:BookTitle>{}</web:BookTitle>
         <web:chapter>{}</web:chapter>
         <web:Verse>{}</web:Verse>
      </web:GetBibleWordsByChapterAndVerse>
   </soapenv:Body>
</soapenv:Envelope>
'''.format(book, chapter, verse)

url = 'http://www.webservicex.net/BibleWebservice.asmx'
headers = {'Content-Type': 'text/xml'}

response = requests.post(url=url, headers=headers, data=request).text

response = response.replace("&gt;", ">").replace("&lt;", "<")

xml_response = et.fromstring(response)

ref = '{} {}:{}'.format(book, chapter, verse)

xmlns = {'xmlns': 'http://www.webserviceX.NET'}
text = xml_response.find('.//xmlns:BibleWords', xmlns).text

print(ref, text)
