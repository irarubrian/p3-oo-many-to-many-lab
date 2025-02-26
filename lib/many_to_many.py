class Author:
    all = []
    def __init__(self, name=str):
        self.name = name

    def contracts(self):
        return[contract for contract in all.contracts if self in contract.author ==self]


    


class Book:
    def __init__(self, title=str):
        self.title = title

    

    


class Contract:
    def __init__(self, author, book, date=str):
        self.author = author
        self.book = book
        self.date = date

    def __init__(self, author, book, date):
        self.author = author
        self.book = book
        self.date = date
        


        

    


    