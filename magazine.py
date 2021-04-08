from Book2 import Book


class Magazine(Book):

    def __init__(self, title, author, publish_year, pages, price, language, issue, pages_read=None, status=None):
        Book.__init__(self, title, author, publish_year, pages, price, language)
        self.issue = issue

    def get_data(number_magazine):
        """ this function get data from the user """
        for i in range(number_magazine):
            print('\033[35Enter information .')
            title = input("Enter title : ")
            author = input("Enter author : ")
            publish_year = int(input("Enter publish_year :"))
            pages = int(input("Enter pages :"))
            language = input("Enter language :")
            price = float(input("Enter price : "))
            issue = int(input("Enter issue :"))
            magazine = Magazine(title, author, publish_year, pages, price, language, issue)
            return magazine
