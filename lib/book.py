#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
       self.title = title
       self._page_count = page_count

    @property
    def page_count(self):
        return self._page_count
    
    @page_count.setter
    def page_count(self,new_page_count):
        '''prints "page_count must be an integer" if page_count is not an integer.'''
        if not isinstance(new_page_count, int):
           print("page_count must be an integer")
        else:
            self._page_count = new_page_count
            
    # def set_book(self, page_count):
    #     if not isinstance(page_count, int):
    #        print("page_count must be an integer")
    #     else:
    #         self.page_count = page_count
    #         return  

    def turn_page(self):
        print("Flipping the page...wow, you read fast!") 
        return self    

# book = Book('Psychology of money', 200)
# print(book.title)
# print(book.page_count)
# print(book.turn_page())