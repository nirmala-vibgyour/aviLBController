from dotenv import load_dotenv
import requests
import os

load_dotenv()

controller=os.getenv("ip")
username=os.getenv("username")
password=os.getenv("password")
version=os.getenv("version")

login = requests.post(f'https://{controller}/api/user/login', json={'username':username, 'password': password}, verify=False)

if login.status_code !=200:
    print(f'Login failed with status code: {login.status_code}')
    print(login.text)
    exit()

print("Login Successful")

csrftoken = login.cookies.get('csrftoken')
sessionid = login.cookies.get('sessionid')

if not csrftoken or not sessionid:
    print("Token or session Id not found.")
    exit()


headers = {
    'Content-Type': 'application/json',
    'X-CSRFToken': csrftoken,
    'X-Avi-Version': version,
    'Referer': f'https://{controller}'
}

cookies = {
    'csrftoken': csrftoken,
    'sessionid': sessionid
}

data = {
    'name': 'nirmala chowdhury-tenant_2'
}

resp = requests.post(f'https://{controller}/api/tenant', headers=headers, json=data, cookies=cookies, verify=False)

if resp.status_code == 200:
    print("Tenant data")
    print(resp.json())
else:
    print(f"Failed with status {resp.status_code}")
    print(resp.text)