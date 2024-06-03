import requests
from bs4 import BeautifulSoup
import csv

url = 'https://proxyway.com/news'
r = requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')

images_list = []

images = soup.select('img')

for image in images:
    src = image.get('src')
    alt = image.get('alt')
    images_list.append({"src": src, "alt": alt})

for image in images_list:
    print(image)
    
with open('data gambar.csv' , 'w', encoding='UTF8') as f:
    writer = csv.writer(f)
    
    writer.writerow(images_list)