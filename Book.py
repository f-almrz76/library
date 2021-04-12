"""This program runs only once time.and you can not go back!"""


class Book:
    bookshelf = []

    def __init__(self, title, author, publish_year, pages, language, price, read_pages=0, status=None):
        self.title = title
        self.author = author
        self.publish_year = publish_year
        self.pages = pages
        self.language = language
        self.price = price
        self.read_pages = read_pages
        self.status = status
        Book.bookshelf.append(self)

    def read(self, pages):
        """ This function get number of pages that you read and calculate how many pages remain."""
        pages = int(pages)
        self.read_pages = pages
        if pages < self.pages:
            print(f"you have read {pages} more pages from {self.title}."
                  f"There are {self.pages - self.read_pages} pages left")
        elif pages == self.pages:
            print(f' {self.title} is finished.')
        else:
            print("you can not read more than book’s pages")

    def __str__(self):
        """ This function returns all information of book . it maybe need later."""
        return f" Title : {self.title}, Author : {self.author}, Publish_year : {self.publish_year}," \
               f" Pages : {self.pages} , Language : {self.language} , Price : {self.price} "

    def get_status(self):
        """This function determines status of book and return it."""
        if self.read_pages == 0:
            self.status = "unread"
        elif self.read_pages == self.pages:
            self.status = "finished"
        else:
            self.status = "reading"
        return self.status


def get_data(number_books):
    """This function get information from user and build a object by them. but first you can set
    how many books you want to add."""
    for i in range(number_books):
        print("----------You can enter information of book.----------")
        title = input(" Enter title : ")
        author = input(" Enter author : ")
        Publish_year = int(input(" Enter publish_year :"))
        pages = int(input(" Enter pages :"))
        Language = input(" Enter language :")
        Price = float(input(" Enter price : "))
        book = Book(title, author, Publish_year, pages, Language, Price)


print("----------Hi welcome to library ----------")
number_book = int(input("How many books do you want to add ? "))
get_data(number_book)
print("---------- You can see your books ----------")
print("Title"+"          "+"Author")
for item in Book.bookshelf:
    print(item.title, "          ", item.author)

choose = input(" if you want to add read_page enter 1 else enter 2 ")
if choose == "1":
    my_book = input(" Which book do you want ?")
    try:
        book = next(item for item in Book.bookshelf if item.title == my_book)
        read_page = int(input(" How many pages do you read ?"))
        book.read(read_page)
    except:
        print(" This book doesn't exist.")
elif choose == "2":
    print("-------------------")

choose = input(" Do you want to see status of books ? if you want see press 1 else press 2")
if choose == "1":
    for item in Book.bookshelf:
        print("Title"+"          "+"Status")
        print(item.title,"          ", item.get_status())
        print("---------- Good lock ----------")
elif choose == "2":
    print("---------- Good lock ----------")
