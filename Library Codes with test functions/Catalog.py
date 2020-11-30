# -*- coding: utf-8 -*-
from Book import Book
#First Book is file & second is Class

class Catalog:
    def __init__(self):
        self.different_book_count = 0
        self.books = []

        
    #Only available to admin
    def addBook(self,name,author,publish_date,pages,isbn):
        b = Book(name,author,publish_date,pages,isbn)
        self.different_book_count += 1
        self.books.append(b)
        print(b.name ,' by ',b.author,' is added to Catalog')
    
    def removeBook(self,name):
        for book in self.books:
            if name.strip() == book.name:
                self.different_book_count -= 1
                self.books.remove(book)
                print(book.name ,' by ',book.author,' is removed from Catalog')

    #Only available to admin
    def addBookItem(self,book,book_num,rack):
        book = self.searchByName(book)
        book.addBookItem(book.name,book_num,rack)
        
    def searchBybookName(self,name):
        for book in self.books:
            if name.strip() == book.name:
                return book.printBook()
    
    def searchByAuthor(self,author):
        for book in self.books:
            if author.strip() == book.author:
                return book.printBook()

    def searchBy_published_date(self,date):
        for book in self.books:
            if date.strip() == book.publish_date:
                return book.printBook()
                #print (book.name,book.author)
                #print ('there are ',len(book.book_item),' copies are left in inventory')

    def search_book_by_isbn(self,isbn):
        for book in self.books:
            if isbn == book.isbn:
                return book.printBook()
    
        
    def displayAllBooks(self):
        print ('There are ',self.different_book_count,' Different Books are there')
        for book in self.books:
            if len(book.book_item) > 0:
                print(book.name,' copies available ',book.total_count)
        
    def removeBookItem(self,name,book_num):
        book = self.searchByName(name)
        book_item = book.searchbynum(book_num)
        book.removeBookItem(name)

    def searchByName(self,name):
        for book in self.books:
            if name.strip() == book.name:
                return book