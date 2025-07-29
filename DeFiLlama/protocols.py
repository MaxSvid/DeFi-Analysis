import requests

base_url = 'https://api.llama.fi'
response = requests.get(base_url + '/protocols')
data = response.json()

       
      
