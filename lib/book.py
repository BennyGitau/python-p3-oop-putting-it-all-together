#!/usr/bin/env python3

class Book:
    def __init__(self, title="Any", page_count=0):
        self.title = title
        self.page_count = page_count
    
    @property
    def page_count(self):
            return self._page_count
        
    @page_count.setter
    def page_count(self, value):
        if isinstance(value, int):
            self._page_count = value
        else:
            print("page_count must be an integer")
        
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

book1 = Book()
print(book1.title)
