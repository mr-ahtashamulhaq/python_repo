#Write a Library class with no_of_books and books as two instance variables. Write a program to create a library from this Library class and show how you can print all books, add a book and get the number of books using different methods. Show that your program doesnt persist the books after the program is stopped!

class Library:
    def _init_(self):
        self.no_of_books = 0     
        self.books = []               

    def add_book(self, book_name):
        self.books.append(book_name)   
        self.no_of_books += 1          

    def print_books(self):
        print("Books in Library:")
        for book in self.books:
            print(book)

    def get_no_of_books(self):
        print("Total number of books:", self.no_of_books)


my_library = Library()


my_library.add_book("Python Programming")
my_library.add_book("Data Structures")
my_library.add_book("Machine Learning Basics")


my_library.print_books()


my_library.get_no_of_books()


print("\nNote: If you run this program again, the books will be lost because the data is stored in RAM only.")