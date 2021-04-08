class Book:
    bookshelf = []

    def __init__(self, title, author, pulish_year, pages, language, price, read_pages=None, statuse = None):
        self.title = title
        self.author = author
        self.pulish_year = pulish_year
        self.pages = pages
        self.language = language
        self.price = price
        Book.bookshelf.append(self)

    def read(self, pages):
        pages=int(pages)
        self.read_pages=pages
        if pages < self.pages:
            print(f"you have read {pages} more pages from {self.title}."
                  f"There are {self.pages-self.read_pages} pages left")
        elif pages == self.pages :
            print(f' {self.title} is finished.')
        else:
            print( "you can not read more than book’s pages")

    def __str__(self):
        return f" Title : {self.title}, Author : {self.author}, Pulish_year : {self.pulish_year}," \
               f" Pages : {self.pages} , Language : {self.language} , Price : {self.price} "

    def get_status(self):
        if self.read_pages==0:
            self.statuse="unread"
        elif self.read_pages == self.pages :
            self.statuse = "finished"
        else:
            self.statuse = "reading"
        return self.statuse



def get_data (number_books):
    for i in range(number_books ):
        title = input(" Enter title : ")
        author = input(" Enter author : ")
        Publish_year =int(input(" Enter pulish_year :"))
        pages =int (input(" Enter pages :"))
        Language = input(" Enter language :")
        Price = float(input(" Enter price : "))
        book = Book(title , author , Publish_year , pages , Language , Price)

get_data(1)
Print_bookshelf=[print(i) for  i in Book.bookshelf]
book_shelf=Book.bookshelf
book_shelf[0].read(11)
print(book_shelf[0].get_status())