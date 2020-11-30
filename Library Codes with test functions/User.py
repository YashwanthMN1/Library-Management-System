# -*- coding: utf-8 -*-
from datetime import date
import Catalog 
from Book import Book

book_list = []
issued_book_list = []
issued_book_data = []

class User:
    def __init__(self, name, location, age, aadhar_id):
        self.name = name
        self.location = location
        self.age = age
        self.aadhar_id = aadhar_id
        

class Member(User):
    def __init__(self,name, location, age, aadhar_id,student_id):
        super().__init__(name, location, age, aadhar_id)
        self.student_id = student_id
        
    def searchbyname(self,name):
        for book in book_list:
            if name == book.name:
                return book

    def __repr__(self):
        return self.name + ' ' + self.location + ' ' + self.student_id
    
    def check_availablity(self,name):
        book = self.searchbyname(name)
        if book.total_count > 0:
            print(book.name," by ",book.author," is available now")
            print('there are ',book.total_count,' number of copies are there')
        elif book.total_count == 0:
            print('This book is not available now')

    def available_books(self):
        print('these books are available now')
        for book in book_list:
            if book.total_count > 0:
                print(book.name ,' by ',book.author,' is availble with ',book.total_count,' number of copies')

    #assume name is unique
    def issueBook(self,name,days=10):
        self.days = days
        for book in book_list:
            if name.strip() == book.name and book.total_count > 0:
            	print(self.name,' you have issued',book.name,' by ',book.author,'for Yourself')
            	book.removeBookItem(book.name)
            	issued_book_list.append([book.name,book.rack])
            	today = date.today()
            	issued_book_data.append([book.name,book.author,self.name,self.student_id,today])
            elif name.strip() == book.name and book.total_count == 0:
            	print('sorry ',name,' This book is not-available right now ,Please try again after some time')        

    #assume name is unique
    def returnBook(self,name):
    	book = self.searchbyname(name)
    	if name.strip() == book.name:
    		x=''
    		for i in issued_book_list:
    			if i[0] == name:
    				x += i[1]
    				issued_book_list.remove(i)
    				print('Thank you',self.name , 'for using our library service')
    		a = book.total_count+1
    		book.addBookItem(book.name,a,x)
    		
    	elif name.strip() != book.name:
            print('    named book not-found')
            print('-->check for spelling mistakes in book name')
        
class Librarian(User):
    def __init__(self,name, location, age, aadhar_id,emp_id):
        super().__init__(name, location, age, aadhar_id)
        self.emp_id = emp_id
        
        
    def __repr__(self):
        return self.name + self.location + self.emp_id


    def searchbyname(self,name):
        for book in book_list:
            if name == book.name:
                return book


    def addBook(self,name,author,publish_date,pages,isbn):
        b = Book(name,author,publish_date,pages,isbn)
        book_list.append(b)
        
    def addBookItem(self,name,book_num,rack):
    	book = self.searchbyname(name)
    	book.addBookItem(book.name,book_num,rack)

    def removeBookItem(self,name,book_num):
        book = self.searchbyname(name)
        book.removeBookItem(book.name)

    def removeBook(self,name):
        book = self.searchbyname(name)
        if name.strip() is book.name:
            book_list.remove(book)
            
    
    def add_book_to_catalog(self,catalog,name):
        book = self.searchbyname(name)
        catalog.addBook(book.name,book.author,book.publish_date,book.pages,book.isbn)
        c= book.total_count
        for item in range(c):
        	catalog.addBookItem(book.name,item,book.rack)
        
    def remove_book_from_catalog(self,catalog,name):
        book = self.searchbyname(name)
        catalog.removeBook(book.name)

    def addBookItemtocatalog(self,catalog,book,book_num,rack):
        catalog.addBookItem(book,book_num,rack)

    def removeBookItemFromCatalog(self,catalog,book,book_num):
        name = ''
        Catalog = catalog
        for Book in Catalog.books:
            if book == Book.name:
                name += Book.name
        catalog.removeBookItem(name,book_num)

class pattern_recognition:
        
	def popular_books(self):
		lst = []
		for data in issued_book_data:
			lst.append(data[0])
		st =set(lst)
		count = []
		for i in st:
			x = lst.count(i)
			count.append([x,i])
		sorted_count = sorted(count,reverse=True)
		for i in sorted_count[:5]:
			print(i[1],'have',i[0],'readers')

	def popular_authors(self):
		lst = []
		for data in issued_book_data:
			lst.append(data[1])
		st =set(lst)
		count = []
		for i in st:
			x = lst.count(i)
			count.append([x,i])
		sorted_count = sorted(count,reverse=True)
		for i in sorted_count[:5]:
			print('Author',i[1],'have',i[0],'readers')

	def good_readers(self):
		lst = []
		for data in issued_book_data:
			lst.append(data[2])
		st =set(lst)
		count = []
		for i in st:
			x = lst.count(i)
			count.append([x,i])
		sorted_count = sorted(count,reverse=True)
		for i in sorted_count[:5]:
			print('student',i[1],'have readed',i[0],'books')
        



