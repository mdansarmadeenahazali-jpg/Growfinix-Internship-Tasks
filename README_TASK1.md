# Growfinix Task 1 – Automated Web Scraper for Property Listings

## Objective

This project is a Python-based web scraper that extracts property listing information from a public real-estate website.

## Technologies

- Python
- Requests
- BeautifulSoup4
- CSV

## Information Extracted

- Property Title
- Price
- Location

## How It Works

1. The program sends a request to a public real-estate webpage.
2. BeautifulSoup4 parses the webpage.
3. Property titles, prices, and locations are extracted.
4. The extracted information is cleaned.
5. The data is saved into a CSV file.

## Files

- property_scraper.py
- properties.csv
- code_task1.png
- output_task1.png
- csv_task1.png

## Run
The program successfully extracted 30 property listings and saved the data to `properties.csv`.
```bash
py property_scraper.py
