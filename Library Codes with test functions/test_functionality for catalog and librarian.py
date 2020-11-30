from Book import Book
from Catalog import Catalog
from User import Member, Librarian


catalog = Catalog()


librarian = Librarian("Awantik","Bangalore",34,'asljlkj22','zeke101') 


'''
librarian.addBook('Moonwalking with Einstien','J Foer', '2017',318,123)
librarian.add_book_to_catalog(catalog,'Moonwalking with Einstien')

catalog.searchBybookName('Moonwalking with Einstien')

librarian.addBookItemtocatalog(catalog,'Moonwalking with Einstien',1,'H1B3')

catalog.searchBybookName('Moonwalking with Einstien')

'''




librarian.addBook('Shoe Dog','Phil Knight','2015',312,456)

librarian.addBookItem('Shoe Dog',1,'H1B2')
librarian.addBookItem('Shoe Dog',2,'H1B2')
librarian.addBookItem('Shoe Dog',3,'H1B2')
librarian.addBookItem('Shoe Dog',4,'H1B2')
librarian.addBookItem('Shoe Dog',5,'H1B2')





librarian.add_book_to_catalog(catalog,'Shoe Dog')
catalog.searchBybookName('Shoe Dog')
catalog.searchBybookName('Shoe Dog')
catalog.searchByAuthor('Phil Knight')
catalog.searchBy_published_date('2015')
catalog.search_book_by_isbn(456)



catalog.displayAllBooks()
