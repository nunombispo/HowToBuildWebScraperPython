import requests
from bs4 import BeautifulSoup
import csv


url = 'https://books.toscrape.com/'
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    print("Page fetched successfully!")
else:
    print(f"Failed to fetch page. Status code: {response.status_code}")


soup = BeautifulSoup(response.content, 'html.parser')
print(soup.prettify())  # This will display the HTML structure


titles = soup.find_all('h3')
for title in titles:
    print(title.a['title'])


prices = soup.find_all('p', class_='price_color')
for price in prices:
    print(price.text)


availability = soup.find_all('p', class_='instock availability')
for stock in availability:
    print(stock.text.strip())


with open('books.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'Price', 'Availability'])  # Write the header

    for title, price, stock in zip(titles, prices, availability):
        writer.writerow([title.a['title'], price.text, stock.text.strip()])
