import requests
from bs4 import BeautifulSoup
import csv

# Public real-estate listing page
url = "https://www.pisos.com/venta/pisos-cedeira/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers, timeout=15)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

properties = []

# Find property cards
listings = soup.select("div.ad-preview")

for listing in listings:
    title = listing.get_text(" ", strip=True)

    price = ""
    location = ""

    # Look for price and location text
    text = listing.get_text(" ", strip=True)

    if "€" in text:
        parts = text.split("€", 1)
        price = parts[0].strip() + " €"

    location = text

    properties.append({
        "Title": title,
        "Price": price,
        "Location": location
    })

# Save data to CSV
with open("properties.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=["Title", "Price", "Location"]
    )

    writer.writeheader()
    writer.writerows(properties)

print("====================================")
print("PROPERTY SCRAPER")
print("====================================")
print("Listings found:", len(properties))
print("Data saved to properties.csv")
print("====================================")