from colorama import Fore
from Media import Media
"""This class inherits from Media."""


class Book(Media):
    books_shelves = []

    def __init__(self, title, author, publish_year, pages, price, language, pages_read=0, status=None, progress=0):
        Media.__init__(self, title, author, publish_year, price, language)
        self.pages = pages
        self.pages_read = pages_read
        self.status = status
        self.progress = progress

    def read(self, pages):
        """ This function get number of pages that you read and calculate how many pages remain.
            it calculates progress too."""
        self.pages_read = pages

        if pages < self.pages:
            print(Fore.WHITE + f"you have read {pages} more pages from {self.title}."
                  f"There are {self.pages-self.pages_read} pages left")
        elif pages == self.pages:
            print(Fore.WHITE +f' {self.title} is finished.')
        else:
            print(Fore.WHITE +"you can not read more than book’s pages")
        """We call function get_status for updating status.and uses it for calculating progress."""
        self.get_status()
        if self.status == "finished":
            self.progress = 100
        else:
            self.progress = (self.pages_read * 100) / self.pages

    def get_status(self):
        """ This function checks out status. and returns it """
        if self.pages_read == 0:
            self.status = "unread"
        elif self.pages_read >= self.pages:
            self.status = "finished"
        else:
            self.status = "reading"
        return self.status


def get_data():
    """This function get information from user and build a object by them. """
    print('\033[35mEnter information.')
    title = input("Enter title : ")
    author = input("Enter author : ")
    publish_year = int(input("Enter publish_year :"))
    pages = int(input("Enter pages :"))
    language = input("Enter language :")
    price = float(input("Enter price : "))
    book = Book(title, author, publish_year, pages, language, price)
    Book.books_shelves.append(book)
    return book

