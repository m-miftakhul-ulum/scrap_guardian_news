from curl_cffi import requests
from bs4 import BeautifulSoup
import re
import dataset
from dataclasses import asdict
from model import News
import pandas as pd

# simpan ke sqlite
# buat fitur query
# buat pilihan penyimpanan


data = []


def get_content(url):
    html_content = requests.get(url, impersonate='chrome').text
    soup = BeautifulSoup(html_content, "html.parser")

    content = soup.find("div", class_="article-body-commercial-selector")
    return content.text


def get_url():
    html_content  = requests.get('https://www.theguardian.com/uk/sport', impersonate='chrome').text
    
    # with open("index.html", "r") as file:
    #     html_content = file.read()
    soup = BeautifulSoup(html_content, "html.parser")

    judulContiner = soup.findAll("h3", class_="card-headline")

    for judul in judulContiner:
        title = judul.find("span").text
        cleaned_title = re.sub(r"\s+", " ", title).strip()

        try:
            coba = soup.find("a", {"aria-label": f"{cleaned_title}"})
            link = coba.get("href")
            data.append({
                "title": cleaned_title, 
                "url":  f"https://www.theguardian.com{link}",
                "content" : get_content(f"https://www.theguardian.com{link}")
            })
        except:
            continue


def save(data):
    db = dataset.connect('sqlite:///mydatabase.db')
    table = db['news_tabel']
    
    for i in data:
        model = News(title=i["title"], url=i["url"], content=i["content"])    
        table.insert(asdict(model))

    
    return "Data berhasil disimpan"
    
    


if __name__ == "__main__":    
    
    action = [
        "1. Get Data",
        "2. Save Data",
        "3. Show Data",
    ]
    print("\n".join(action))
    
    input_data = input("pilih nomor: ")
    
    if input_data == "1":
        get_url()
    elif input_data == "2":
        save(data)    
    elif input_data == "3":
        db = dataset.connect('sqlite:///mydatabase.db')
        table = db['news_tabel']
        for row in table.all():
            print(row)
    
