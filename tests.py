#tests

from main import getListing
from main import getChoice
from main import getISBN
from main import downloadBook
from main import getBook
from book import Book
title="Of Mice and Men"

def testListing() :
    #print(getListing(title))
    titles=getListing(title)

    for x in range(len(titles)) :
    
        print(x,":", titles[x].text)


def testChoice() :
    choice=getChoice(getListing(title))
    print(choice)

def testISBN() :
    book=getListing(title)[0]
    isbn=getISBN(book)
    print(isbn)

def testDownload() :
    book=getBook(title)
    downloadBook(book)
def testGetBook() :
    book=getBook(title)
    print(book.title, book.url, book.filetype)
def test() :
    #testListing()
    #testChoice()
    #testISBN()
    #testGetBook()
    testDownload()
test()