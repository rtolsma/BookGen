# Main execution file for bookgen project
import argparse
import requests
from bs4 import BeautifulSoup
import re
from book import Book
'''
Structure:

1. Parse Title Arguments+download path
2. Scrape Top X titles (or 1st page) w/ urls on Amazon with msoup
3. User selects title option
4. Scrape ISBN13 with msoup of title
5. Automate download from libgen if exists
6. If no results for ISBN13 OR no ISBN13 exists then
directly search on libgen and provide same set of choices


'''
'''
Possible program arguments:

Auto vs. User Choice
Download Path
Title/ISBN
'''


AMZN="http://www.amazon.com/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords="
LIBGEN_SEARCH="http://libgen.io/search.php?req={}&lg_topic=libgen&open=0&view=simple&res=25&phrase=1&column=def"
LIBGEN="http://libgen.io/"
TITLE_CLASS="a-link-normal s-access-detail-page s-color-twister-title-link a-text-normal"

def main():
    # Parse arguments
    parser = argparse.ArgumentParser(description="Book Title")
    parser.add_argument("title")
    args = parser.parse_args()

    title = args.title
    try:
        books = getListing(title)

        choice = getChoice(books)
        bookISBN = getISBN(books)

        downloadBook(bookISBN)  # path
    except:
        print("error")


def getListing(title):
    page=requests.get(AMZN+title)
    soup=BeautifulSoup(page.content,"html.parser")
    #scrape results data

    results=soup.findAll(id=re.compile("result_[0-9]"))
    results=results[0:2] #testing limit to 2
    #results=soup.findAll("a", class_=TITLE_CLASS)
    books=[]
    for result in results :
        bookHTML=result.find("a", class_=TITLE_CLASS)
        books.append(Book(bookHTML.text, bookHTML["href"]))
        
    return books
    


# returns the book chosen
def getChoice(books):
    
    for x in range(len(books)) :
        print(x+1,":", books[x].title)
    
    userInput=-1
    while userInput<0 or userInput>len(books) :
        try:
            userInput=int(input("Enter your choice [1-{}] : ".format(len(books))))

        except ValueError:
            print("Input must be a valid integer between [1-{}]".format(len(books)))
            continue
    
    
    choice=books[userInput-1]
    return choice

def getISBN(book):
    bookPage=requests.get(book.url)
    ISBN13=re.search("978-[0-9]+", bookPage.text).group(0)

    return ISBN13


#Can take in ISBN or titles
def getBook(search, ISBN=False, decide=False): 
    
    if ISBN :
        libpage=requests.get(LIBGEN_SEARCH.format(ISBN))
    else :
        libpage=requests.get(LIBGEN_SEARCH.format(search))
    
    
    
    soup=BeautifulSoup(libpage.content, "html.parser")
    resultsTable=soup.findAll("table")[2]
    tableRows=resultsTable.findAll("tr")[1:]

    books=[]
    #shitty code follows
    for x in range(len(tableRows)):
        row=tableRows[x]
        cells=row.findAll("td")
        url=LIBGEN+cells[2].find("a")["href"]
        title=cells[2].find("a").text
        filetype=cells[8].text
        book=Book(title, url, filetype)
        books.append(book)
    
    if decide :
        choice=getChoice(books)
    else :
        choice=books[0]
    
    return choice


def downloadBook(book, path=None) :
    page=requests.get(book.url)
    soup=BeautifulSoup(page.content, "html.parser")
    lastLink=soup.find("a", text="Libgen.io")["href"]

    downloadPage=requests.get(lastLink)
    soup=BeautifulSoup(downloadPage.content,"html.parser")

    #download link
    bookFile=requests.get(soup.find("a",text="DOWNLOAD")["href"],stream=True)
    #Writes the downloaded file to system as it downloads
    with open(book.title, "wb") as f:
        for chunk in bookFile.iter_content(chunk_size=1024): 
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)

    print("Download Finished")

    #print(resultsTable)


if __name__ == "__main__":
    main()
