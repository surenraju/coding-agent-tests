class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True

    def __str__(self):
        status = "Available" if self.available else "Checked out"
        return f"'{self.title}' by {self.author} (ISBN: {self.isbn}) - {status}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, isbn):
        """Add a new book to the library collection"""
        # Check if book with same ISBN already exists
        for book in self.books:
            if book.isbn == isbn:
                return False  # Book with same ISBN already exists
        
        new_book = Book(title, author, isbn)
        self.books.append(new_book)
        return True

    def remove_book(self, isbn):
        """Remove a book from the library by ISBN"""
        for i, book in enumerate(self.books):
            if book.isbn == isbn:
                del self.books[i]
                return True
        return False

    def search_books(self, query):
        """Search for books by title or author (case-insensitive, partial matches)"""
        results = []
        query = query.lower()
        
        for book in self.books:
            if (query in book.title.lower() or 
                query in book.author.lower()):
                results.append(book)
        
        return results

    def check_out_book(self, isbn):
        """Check out a book (mark as unavailable)"""
        for book in self.books:
            if book.isbn == isbn:
                if book.available:
                    book.available = False
                    return True
                return False  # Book is already checked out
        return False  # Book not found

    def return_book(self, isbn):
        """Return a book (mark as available)"""
        for book in self.books:
            if book.isbn == isbn:
                if not book.available:
                    book.available = True
                    return True
                return False  # Book is already available
        return False  # Book not found

    def display_all_books(self):
        """Display all books with their current status"""
        if not self.books:
            print("No books in the library.")
        else:
            for book in self.books:
                print(book)