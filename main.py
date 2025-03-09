from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup
import pandas as pd

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Amazon Price Tracker API"}

@app.get("/scrape")
def scrape_amazon(url: str):
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    title = soup.find("span", {"id": "productTitle"}).text.strip()
    price = soup.find("span", {"class": "a-price-whole"})
    price = price.text.strip() if price else "Not Available"

    return {"title": title, "price": price}