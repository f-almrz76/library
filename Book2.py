from Media import Media


class Book(Media):

    def __init__(self, title, author, publish_year, pages, price, language, pages_read=None, status=None, progress=0):
        Media.__init__(self, title, author, publish_year, price, language)
        self.pages = pages
        self.pages_read = pages_read
        self.status = status
        self.progress = progress

    def read(self, pages):
        self.pages_read = pages
        self.progress = (self.pages_read * 100) / self.pages
        if pages < self.pages:
            print('\033[29m'+f"you have read {pages} more pages from {self.title}."
                  f"There are {self.pages-self.pages_read} pages left")
        elif pages == self.pages:
            print('\033[29m'+f' {self.title} is finished.')
        else:
            print('\033[29m'+"you can not read more than book’s pages")
        self.get_status()

    def get_status(self):
        """ this function is status at each time """
        if self.pages_read == 0:
            self.status = "unread"
        elif self.pages_read == self.pages:
            self.status = "finished"
        else:
            self.status = "reading"
        return self.status

    def get_data(number_books):
        """ this function get data from the user """
        bookshelf = []
        for i in range(number_books):
            print('\033[35mEnter information.')
            title = input("Enter title : ")
            author = input("Enter author : ")
            publish_year = int(input("Enter publish_year :"))
            pages = int(input("Enter pages :"))
            language = input("Enter language :")
            price = float(input("Enter price : "))
            book = Book(title, author, publish_year, pages, language, price)
            return book

