import requests

controller=""
username=""
password=""

login = requests.post(f'https:://{controller}/login', data={'username':'', 'password':''}, verify=False)

if login.status_code !=200:
    print(f'Login failerd with status code: {login.status_code}')
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
    'X-Avi-Version': '',
    'Referer': f'https://{controller}'
}

cookies = {
    'csrftoken': csrftoken,
    'sessionid': sessionid
}

resp = requests.get(f'https://{controller}/api/tenant', headers=headers, cookies=cookies,verify=False)

if resp.status_code == 200:
    print("Tenant data")
    print(resp.json())
else:
    print(f"Failed with status {resp.status_code}")
    print(resp.text)