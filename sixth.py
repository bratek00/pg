import sys
import requests
import re


def download_url_and_get_all_hrefs(url):
    """
    Funkce stahne url predanou v parametru url pomoci volani response = requests.get(),
    zkontroluje navratovy kod response.status_code, ktery musi byt 200,
    pokud ano, najdete ve stazenem obsahu stranky response.content vsechny vyskyty
    <a href="url">odkaz</a> a z nich nactete url, ktere vratite jako seznam pomoci return
    """
    try:
        response = requests.get(url)
        if response.status_code != 200:
            raise ValueError(f"Server returned status code {response.status_code}")

        content = response.text

        hrefs = re.findall(r'<a[^>]+href="([^"]+)"', content)

        return hrefs
    except Exception as e:
        print(f"Chyba při stahování stránky: {e}")
        return []


if __name__ == "__main__":
    try:
        
        if len(sys.argv) < 2:
            raise ValueError("Zadejte URL jako první argument!")

        url = sys.argv[1]
        hrefs = download_url_and_get_all_hrefs(url)

        if hrefs:
            print("Nalezené odkazy:")
            for href in hrefs:
                print(href)
        else:
            print("Na stránce nebyly nalezeny žádné odkazy.")

    except Exception as e:
        print(f"Program skončil chybou: {e}")
