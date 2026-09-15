import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

BASE_URL = "https://books.toscrape.com/catalogue/"

books = []

print("Starting web scraping...")

for page in range(1, 6):

    url = f"{BASE_URL}page-{page}.html"

    print(f"Scraping page {page}...")

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        book_items = soup.select("article.product_pod")

        for book in book_items:

            title = book.h3.a["title"]

            price = book.select_one(".price_color").text.strip()

            availability = book.select_one(".availability").text.strip()

            rating = book.select_one("p.star-rating")["class"][1]

            book_link = book.h3.a["href"]

            book_url = BASE_URL + book_link.replace("../", "")

            books.append({
                "Title": title,
                "Price": price,
                "Rating": rating,
                "Availability": availability,
                "Book_URL": book_url
            })

        time.sleep(1)

    except requests.RequestException as e:
        print(f"Error while scraping page {page}: {e}")


df = pd.DataFrame(books)

df.to_csv("scraped_books.csv", index=False, encoding="utf-8-sig")


print("\nScraping completed successfully!")
print(f"Total books scraped: {len(df)}")
print("Data saved as: scraped_books.csv")

print("\nFirst 5 records:")
print(df.head())