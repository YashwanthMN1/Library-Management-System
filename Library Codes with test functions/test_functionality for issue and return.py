from Book import Book
import Catalog
from User import Member,Librarian
import User


m1 = Member("Vish","Bangalore",23,'asljlkj22','std1233')
librarian = Librarian("Awantik","Bangalore",34,'asljlkj22','zeke101') 




librarian.addBook('Moonwalking with Einstien','J Foer', '2017',318,123)
librarian.addBookItem('Moonwalking with Einstien',1,'H1B3')
librarian.addBook('Shoe Dog','Phil Knight','2015',312,456)

librarian.addBookItem('Shoe Dog',1,'H1B2')
librarian.addBookItem('Shoe Dog',2,'H1B2')
librarian.addBookItem('Shoe Dog',3,'H1B2')
librarian.addBookItem('Shoe Dog',4,'H1B2')
librarian.addBookItem('Shoe Dog',5,'H1B2')

#m1.available_books()

#m1.check_availablity('Shoe Dog')


print(User.issued_book_list,' issued list')
print(User.issued_book_data,' issued data')

m1.issueBook('Moonwalking with Einstien')
print(User.issued_book_list,' issued list')
print(User.issued_book_data,' issued data')

m1.returnBook('Moonwalking with Einstien')
print(User.issued_book_list,' issued list')
print(User.issued_book_data,' issued data')
