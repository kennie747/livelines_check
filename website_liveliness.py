import requests
import time

def check_website(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return True
    except requests.exceptions.RequestException:
        return False

def main():
    url = 'https://example.com'
    while True:
        if check_website(url):
            print(f'{url} is up!')
        else:
            print(f'{url} is down!')
        time.sleep(60)

if __name__ == '__main__':
    main()
