import json
import requests
from bs4 import BeautifulSoup

SHARED_HEADER = {
    'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    'Referer': 'alpari.com'
}


class Alpari:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.login()

    def login(self):
        url = "https://alpari.com/api/en/auth/login/"
        payload = {
            "login": self.email,
            "password": self.password,
            "saveShowingUserName": True
        }
        payload = json.dumps(payload)
        headers = {
            **SHARED_HEADER,
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/json;charset=UTF-8',
            'host': 'alpari.com',
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        self.ssid = response.cookies['ssid']
        self.ssid_api = response.cookies['ssid_api']

    def get_acounts_list(self):
        accounts = {}
        url = "https://my.alpari.com/en/investments/pamm_accounts/"

        payload = {}
        headers = {
            **SHARED_HEADER,
            'Upgrade-Insecure-Requests': '1',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'host': 'my.alpari.com',
            'Cookie': f'already_client=1; ssid={self.ssid}; ssid_api={self.ssid_api}'
        }
        response = requests.request("GET", url, headers=headers, data=payload)

        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        account_list_div = soup.find(
            'div', class_='investment-account-list-items')

        if account_list_div:
            # Find all elements with class 'name' and 'equity' within the selected div
            name_elements = account_list_div.find_all(class_='name')
            equity_elements = account_list_div.find_all(class_='equity')

            # Iterate through the elements and extract the text
            for name, equity in zip(name_elements, equity_elements):
                name_text = name.get_text()
                equity_text = equity.get_text()
                accounts[name_text] = equity_text
        else:
            print("The 'investment-account-list-items' div was not found in the HTML.")
        return accounts
