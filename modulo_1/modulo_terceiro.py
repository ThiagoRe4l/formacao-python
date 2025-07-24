# pip3 install requests==2.31.0

print("\nImportação e uso de um módulo de terceiros")
import requests

url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(url)
print(f"Solicitacao HTTP para {url} retornou o status {response.status_code}")