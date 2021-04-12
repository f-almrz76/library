"""This is main class.it has same attribute that we have."""


class Media:


    def __init__(self, title, publish_year, price, language, author=None, status=None):
        self.title = title
        self.author = author
        self.publish_year = publish_year
        self.price = price
        self.language = language
    """ This function returns all information of Media . it maybe need later."""
    def __str__(self):
        return f"Title : {self.title}, Author : {self.author}, Publish_year : {self.publish_year}" \
               f"Price : {self.price} , Language : {self.language}"


