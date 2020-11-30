# -*- coding: utf-8 -*-
class BookItem:
    def __init__(self,name,book_num,rack):
        self.book_name = name
        self.book_num = book_num
        self.rack = rack
    
    def __repr__(self):
        return self.book_name + ',' + str(self.book_num) + ',' + self.rack 
