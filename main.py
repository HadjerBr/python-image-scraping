from bs4 import BeautifulSoup
import requests
import urllib.request # to download from source attr links

result = requests.get("https://unsplash.com/s/photos/cat", headers = {'User-Agent': 'Mozilla/5.0'})
soup = BeautifulSoup(result.text, "lxml")
images = soup.find_all("img", {"data-test" : "photo-grid-single-col-img"})

urls= []
for image in images:
    url = image["src"]
    urls.append(url)
    print(url)


for i in range(len(urls)):
    name = f"C:\\Users\\orange\\OneDrive\\Documents\\3rd year computer engineering\\python scraping and downloading images\\images\\{i}.jpg"
    urllib.request.urlretrieve(urls[i], name)