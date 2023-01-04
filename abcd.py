import requests
import json

def main():
    
    content = requests.get("https://cve.circl.lu/api/limit")
    
    j = content.json()
    
    for item in j:
        
        print("{} {}".format("Vuln Num:", item['id']))
        print("{} {}\n".format("Description:", item ['summary']))
        
        
main()

