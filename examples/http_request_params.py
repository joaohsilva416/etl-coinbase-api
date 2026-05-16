import requests

url = 'https://jsonplaceholder.typicode.com/comments'
params = {'postId': 1}

response = requests.get(url, params=params)
posts = response.json()

print(f'Total de {len(posts)} posts encontrados')
print(f'Error: {response.status_code} - {response.text}')