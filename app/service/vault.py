import requests
from export.env import VAULT_TOKEN


class Vault:
    def __init__(self):
        self.url = 'http://192.168.60.152:8200/'
        self.headers = {
            'Content-Type': 'application/json',
            'X-Vault-Token': VAULT_TOKEN
        }
    
    def get_secret(self, path):
        response = requests.get(self.url + path, headers=self.headers)
        if response.status_code == 200:
            r = response.json() 
            return r['data']['data']
        return None

    def write_secret(self, path, data):
        response = requests.post(self.url + path, headers=self.headers, json=data)
        return response.json()
