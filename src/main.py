from curl_cffi import requests
from bs4 import BeautifulSoup
import re
import dataset
from dataclasses import asdict
from model import News
import sqlite3
import pandas as pd


data = []


def get_content(url):
    html_content = requests.get(url, impersonate="chrome").text
    soup = BeautifulSoup(html_content, "html.parser")

    content = soup.find("div", class_="article-body-commercial-selector")
    return content.text


def get_url():
    html_content = requests.get(
        "https://www.theguardian.com/uk/sport", impersonate="chrome"
    ).text

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
            data.append(
                {
                    "title": cleaned_title,
                    "url": f"https://www.theguardian.com{link}",
                    "content": get_content(f"https://www.theguardian.com{link}"),
                }
            )
        except:
            continue


def save(data):
    db = dataset.connect("sqlite:///mydatabase.db")
    table = db["news_tabel"]

    for i in data:
        model = News(title=i["title"], url=i["url"], content=i["content"])
        table.insert(asdict(model))

    return "Data berhasil disimpan"


def save_choice():

    conn = sqlite3.connect("mydatabase.db")
    query = "SELECT * FROM news_tabel"
    df = pd.read_sql_query(query, conn)
    conn.close()
    save = input("Pilihan penyimpanan (1. Excel, 2. CSV, 3. JSON): ")
    if save == "1":
        df.to_excel("data.xlsx", index=False)  # Simpan ke Excel
        print("Data berhasil disimpan ke file data.xlsx")
    elif save == "2":
        df.to_csv("data.csv", index=False)  # Simpan ke CSV
        print("Data berhasil disimpan ke file data.csv")
    elif save == "3":
        df.to_json("data.json", orient="records", indent=4)  # Simpan ke JSON
        print("Data berhasil disimpan ke file data.json")
    else:
        print("Pilihan tidak tersedia.")

def query(query):
    conn = sqlite3.connect("mydatabase.db")
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df


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
        save_choice()

    elif input_data == "3":
        query_input = input("Masukkan query: ")
        print(query(query_input))
