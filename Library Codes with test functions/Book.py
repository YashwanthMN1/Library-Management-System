# -*- coding: utf-8 -*-
from BookItem import BookItem

class Book:
    def __init__(self,name,author,publish_date,pages,isbn):
        self.name = name
        self.author = author
        self.publish_date = publish_date
        self.pages = pages
        self.isbn = isbn
        self.total_count = 0
        self.book_item = [0]
        self.rack = ''

    def addBookItem(self,name,book_num,rack):
        if name == self.name:
            b = BookItem(name,book_num,rack)
            self.rack = rack
            self.book_item.append(b)
            self.total_count +=1


    def printBook(self):
        #returns number of copies in inventory
        print (self.name,'by',self.author)
        print ('there are ',len(self.book_item)-1,' books are there in inventory')

    def removeBookItem(self,name):
        if name == self.name:
            a=self.book_item[-1]
            self.book_item.remove(a)
            self.total_count -=1
  
    def __repr__(self):
        return self.name + ',' + self.author + ',' + self.publish_date + ',' + str(self.pages)+','+str(self.isbn)

    def __str__(self):
        return self.name

    def searchbynum(self,book_num):
        if self.total_count > book_num:
            print( self.name,book_num,self.rack)


