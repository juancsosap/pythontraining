import requests


json_dict = {"apellido": "Sosa", "nombre": "Jadash", "rut": "24.486.614-k"}

res = requests.post('http://localhost/api/personas', json=json_dict)

if res.ok:
    print(res.json())
