from actions import scrapeAll, scrapeKeywords

print("Hey :) \nWelcome to this simple web scrapper, for now, you have 2 options: \n\n1- Scrape the whole website\n2- Search keywords in quotes\n3- Search keywords in authors\n")
choice = input("    >>> ")

if choice=='1':
    scrapeAll()

elif choice=='2':
    keyword = input("Select the keyword to search: ")
    scrapeKeywords(keyword)