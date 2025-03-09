from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup
import pandas as pd
from backend.database import SessionLocal, Product

# Initialize the FastAPI app
app = FastAPI()

# Root endpoint returning a welcome messaeg
@app.get("/")
def home():
    return {"message": "Amazon Price Tracker API"}

# Endpoint to scrape Amazon product details
@app.get("/scrape")
def scrape_amazon(url: str):
    # Set headers to mimic a browser request
    headers = {"User-Agent": "Mozilla/5.0"} 
    # Send GET request to the provided URL
    response = requests.get(url, headers=headers)
    # Parse the HTML content of the response
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract the product title and price
    title = soup.find("span", {"id": "productTitle"}).text.strip()
    price = soup.find("span", {"class": "a-price-whole"})
    price = price.text.strip() if price else "Not Available"

    return {"title": title, "price": price} # Return extracted title and price

# Endpoint to track a product and save it to the database
@app.pst("/track")
def track_product(url: str):
    # Create a new database session
    session = SessionLocal()
    # Scrape product details from the provided URL
    data = scrape_amazon(url)

    # Create a new Product object and add it to the database session
    product = Product(url=url, title=data["title"], price=float(data["price"].replace(",", "")))
    session.add(product)
    # Commit the session to save the product to the database
    session.commit()

    return {"message": "Product added to database!"} # Return success message