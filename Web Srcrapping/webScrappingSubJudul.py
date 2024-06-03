import requests
from bs4 import BeautifulSoup
import csv

url = 'https://proxyway.com/news'
r = requests.get(url)

if r.status_code == 200:
    soup = BeautifulSoup(r.text, 'html.parser')
    paragraphs = soup.find_all('h2')

    with open ('subjudul.csv', 'w', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)

        for paragraph in paragraphs:
            writer.writerow([paragraph.text])
            print(paragraph.text)

else:
    print('Gagal mengambil halaman:', r.status_code)