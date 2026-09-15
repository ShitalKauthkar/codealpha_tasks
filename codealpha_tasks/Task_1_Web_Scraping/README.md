# CodeAlpha Task 1 - Web Scraping

## Project Title

Web Scraping of Online Bookstore Data Using Python

## Objective

The objective of this project is to collect structured book information from a public website using Python web scraping techniques.

## Website Used

Books to Scrape

## Technologies Used

- Python
- Requests
- BeautifulSoup
- Pandas

## Data Collected

The following information was extracted:

- Book Title
- Price
- Rating
- Availability
- Book URL

## Methodology

1. Send HTTP requests to the website.
2. Parse HTML content using BeautifulSoup.
3. Extract book information from each page.
4. Repeat the scraping process across multiple pages.
5. Store the extracted information in a Pandas DataFrame.
6. Export the final dataset to a CSV file.

## Output

The scraped data is stored in:

`scraped_books.csv`

A total of 100 book records were collected from 5 pages.

## How to Run

Install the required libraries:

```bash
pip install -r requirements.txt
```

Run the Python script:

```bash
python web_scraping.py
```

The scraped dataset will be generated as:

`scraped_books.csv`
