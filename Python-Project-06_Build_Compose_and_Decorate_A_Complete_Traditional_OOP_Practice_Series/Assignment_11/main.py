'''11. Class Methods
Assignment:
Create a class Book with a class variable total_books. Add a class method increment_book_count() to increase the count when a new book is added.'''

# Make Book class
class Book:
    total_books = 0  # class variable to track total books

    def __init__(self, title):
        self.title = title  # set book title
        Book.total_books += 1  # increase book count when a new book is created

    @classmethod
    def show_total_books(cls):
        print(f"Total books added: {cls.total_books}")  # display total book count


# create 3 books
book1 = Book("Atomic Habits")
book2 = Book("The Alchemist")
book3 = Book("Harry Potter")

Book.show_total_books()  # show total books added
