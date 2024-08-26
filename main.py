from app.actions import scrapeAll, scrapeKeywords, scrapeAuthors


print("Hey :) \nWelcome to this simple web scrapper, for now, you have 3 options: \n\n1- Scrape the whole website\n2- Search keywords in quotes\n3- Search Author by Name\n")
choice = input("    >>> ")

if choice=='1':
    scrapeAll()
    print("Done, check scrape.txt :)")

elif choice=='2':
    keyword = input("Select the keyword to search: ")
    scrapeKeywords(keyword)
    print("Done, check scrape.txt :)")

elif choice=='3':
    keyword = input("Select Name: ")
    scrapeAuthors(keyword)
    print("Done, check scrape.txt :)")    

else:
    print("You selected the wrong option :(")