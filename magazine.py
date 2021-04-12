from Book2 import Book
"""This class inherits from Book."""


class Magazine(Book):
    Magazine_shelves=[]

    def __init__(self, title, author, publish_year, pages, price, language, issue, pages_read=0, status=None):
        Book.__init__(self, title, author, publish_year, pages, price, language)
        self.issue = issue


def get_data():
    """This function get information from user and build a object by them."""
    print('\033[35Enter information .')
    title = input("Enter title : ")
    author = input("Enter author : ")
    publish_year = int(input("Enter publish_year :"))
    pages = int(input("Enter pages :"))
    language = input("Enter language :")
    price = float(input("Enter price : "))
    issue = int(input("Enter issue :"))
    magazine = Magazine(title, author, publish_year, pages, price, language, issue)
    magazine.Magazine_shelves.append(magazine)
    return magazine
