from zeep import Client
# pip install zeep

client = Client('http://www.webservicex.net/ConvertSpeed.asmx?WSDL')
result = client.service.ConvertSpeed(100, 'kilometersPerhour', 'milesPerhour')
print(str(result))

client = Client('http://www.webservicex.net/BibleWebservice.asmx?WSDL')
result = client.service.GetBibleWordsByChapterAndVerse('john', 1, 1)
print(result)
