import sys
import requests 

"""
program stahne url a z ni vrati vsechnz nadpisy:
"""
def stahni_url_a_vrat_nadpisy(url):
    nadpisy = []
    try:
        response = requests.get(url)
    except requests.exeptions.ConnectionError:
        print(f"nastaka chyba, nepodarilo se pripojit na {url}")
        return[]
    if response.status_code != 200:
        print(f"nastaka chzba. http code: {response.status_code}")
        return[]
    
    response.conect 

    return nadpisy

if __name__ == "main":
    url = sys.argv[1]
    nadpisy = stahni_url_a_vrat_nadpisy(url)
    print(nadpisy)