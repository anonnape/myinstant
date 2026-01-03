
import os
import requests
from bs4 import BeautifulSoup
import re
from random import randrange

dir = os.getcwd()+"/data"
if not os.path.isdir(dir):
    os.mkdir(dir)
to_url = f"https://www.myinstants.com/categories/memes/?page=*&name=memes"

def download(name, url):
    try:
        main_name = name.replace(".", "").replace("$", "").replace("%", "").replace("*", "").replace("^", "").replace("!", "").replace("/", "")
        print("\r" + f"Downloading : {name}")
        main_name = f"{name}.mp3"
        if main_name in os.listdir(dir):
            main_name = name+f"({randrange(20)})"+".mp3"
        r = requests.get(url)
        main_name = main_name.replace("/", "")                                                                                                                                                                                  
        open(f"{dir}/{main_name}", 'x')
        open(f"{dir}/{main_name}", 'wb').write(r.content)
        print("\r" + f"Downloaded {name}") 
    except Exception as e:
        print(f"Could not download {name}")
        print(e)

a = int(input("No of pages to scrape :"))


print(f"Starting Loop for {a} no. of pages .")
for i in range(0, a):
    i=i+1
    count = str(i)
    get_url = to_url.replace("*", i, 1)
    page = requests.get(get_url)
    soup = BeautifulSoup(page.content, "html.parser")
    name_results = soup.find_all(class_="instant-link")
    url_results = soup.find_all(class_="small-button")
    if len(name_results) == len(url_results):
        print(f"Got The Data for page {i}")
        valid = True
        len_data = len(name_results)
    else:
        print(f"There was a error getting the data for page{i}")

    if valid:
        for u in range(len_data):
            name_result = name_results[u]
            url_result = url_results[u]
            extract = name_result.get_text()

            res = re.search(r'\'.*?\'', str(url_result)) 
            if res:
                reuwu=res.group(0)
            main_url = reuwu.replace("'", "")
            main_url = f"https://www.myinstants.com{main_url}"
            print("\r" + main_url + "\n" + extract)   
            download(extract, main_url)


    print("Saved to :"+dir)
print("Done [(0uO)]")
