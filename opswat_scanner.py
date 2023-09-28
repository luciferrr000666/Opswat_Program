import requests
import json 
import pandas

headers = {"apikey": "API_KEY"}

def scan_domain():
    domain = input("Enter domain: ")
    opswat_domain = f'https://api.metadefender.com/v4/domain/{domain}'
    response = requests.request("GET", opswat_domain, headers=headers)
    decodedResponse = json.loads(response.text)
    return decodedResponse
    
def scan_hash():
    hash_value = input("Enter hash value: ")
    opswat_hash = f'https://api.metadefender.com/v4/hash/{hash_value}'
    response = requests.request("GET", opswat_hash, headers=headers)
    decodedResponse = json.loads(response.text)
    return decodedResponse
    
def scan_ip():
    ip = input("Enter IP address: ")
    opswat_ip = f'https://api.metadefender.com/v4/ip/{ip}'
    response = requests.request("GET", opswat_ip, headers=headers)
    decodedResponse = json.loads(response.text)
    return decodedResponse
    
def scan_url():
    url = input("Enter url: ")
    opswat_url = f'https://api.metadefender.com/v4/url/{url}'
    response = requests.request("GET", opswat_url, headers=headers)
    decodedResponse = json.loads(response.text)
    return decodedResponse

# Scanner dashboard
def dashboard():
    print("\n[+] OPSWAT Metadefender Scanner")
    print("\n[+] Available options")
    print("\n[1] Scan Domain")
    print("\n[2] Scan Hash")
    print("\n[3] Scan IP")
    print("\n[4] Scan Url")

    option = input("\nEnter option to scan: ")
    
    if option == '1':
        result = scan_domain()
        print(result)
    elif option == '2':
        result = scan_hash()
        print(result)
    elif option == '3':
        result = scan_ip()
        print(result)
    elif option == '4':
        result = scan_url()
        print(result)
    else:
        print("Invalid choice")

while True:
    dashboard()