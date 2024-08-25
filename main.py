from bs4 import BeautifulSoup
import requests

output = open("scrape.txt", "w")
page = requests.get("https://quotes.toscrape.com/")

soup = BeautifulSoup(page.content, "html.parser")

quotes = soup.findAll("span", attrs={"class":"text"})
authors = soup.findAll("small", attrs={"class":"author"})

for quote, author in zip (quotes, authors):
    print("Quote: " + quote.text + "\nAuthor: " + author.text + "\n", file=output)

output.close()