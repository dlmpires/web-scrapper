from bs4 import BeautifulSoup
import requests
import re

# Define page that will be scrapped
page = requests.get("https://quotes.toscrape.com/")

# Fetch html page content
soup = BeautifulSoup(page.content, "html.parser")

# Filter quotes and authors
quotes = soup.findAll("span", attrs={"class":"text"})
authors = soup.findAll("small", attrs={"class":"author"})

# This function starts by opening a .txt file to store the information, and then runs a for loop that stores all quotes and authors on the file
def scrapeAll():
    with open("scrape.txt", "w") as output:
        for quote, author in zip (quotes, authors):
            print("Quote: " + quote.text + "\nAuthor: " + author.text + "\n", file=output)

# The for loop searches for quotes with a keyword (re.search) and then re.sub replaces the keyword to Uppercase
def scrapeKeywords(keyword):
    with open("scrape.txt", "w") as output:
        for quote in quotes:
            if re.search(keyword, quote.text, re.IGNORECASE):
                highlighted_quote = re.sub(f"({keyword})", keyword.upper(), quote.text, re.IGNORECASE)
                print(highlighted_quote, file=output)