from Book import Book


b1 = Book('Shoe Dog','Phil Knight', '2015',312,1234)




b1.addBookItem('Shoe Dog',1,'H1B2')
b1.addBookItem('Shoe Dog',2,'H1B2')
b1.addBookItem('Shoe Dog',3,'H1B2')
b1.addBookItem('Shoe Dog',4,'H1B2')
b1.addBookItem('Shoe Dog',5,'H1B2')


'''
b1.printBook()
b1.removeBookItem('Shoe Dog')
b1.printBook()
'''

b1.searchbynum(2)
