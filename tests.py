#tests

from main import getListing
from main import getChoice
from main import getISBN
from main import downloadBook
from main import getBook
from book import Book
import time

title="The Hobbit"

def testListing() :
    #print(getListing(title))
    titles=getListing(title)

    for x in range(len(titles)) :
    
        print(x,":", titles[x].title)


def testChoice(books) :
    choice=getChoice(books)
    print(choice)

def testISBN(book) :
    isbn=getISBN(book)
    print(isbn)

def testDownload(book) :
    downloadBook(book)

def testGetBook(search) :
    book=getBook(search)[0]
    print(book.title, book.url, book.filetype)

def testTime( testFunction,param=None):
    now=time.time()
    if param :
        testFunction(param)
    else :
        testFunction()
    print("It took", time.time()-now, "seconds to execute: ", testFunction)

def test() :
    books=getListing(title)
    book=getBook(title)[0]
    isbn=getISBN(books[0])
    #testTime(testListing)
    testTime(testISBN , book)
   # testTime(testGetBook,isbn)
    print("Using title")
    testTime(testGetBook,title)
    testTime(downloadBook,book)
test()