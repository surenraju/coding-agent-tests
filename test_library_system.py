from library_management import Library

def main():
    # Create a library instance
    library = Library()
    
    print("=== Library Management System Demo ===\n")
    
    # Add some books
    print("1. Adding books to the library:")
    library.add_book("The Great Gatsby", "F. Scott Fitzgerald", "978-0-7432-7356-5")
    library.add_book("To Kill a Mockingbird", "Harper Lee", "978-0-06-112008-4")
    library.add_book("1984", "George Orwell", "978-0-452-28423-4")
    library.add_book("Pride and Prejudice", "Jane Austen", "978-0-14-143951-6")
    
    # Display all books
    print("\n2. All books in the library:")
    library.display_all_books()
    
    # Search for books
    print("\n3. Searching for books with 'the' in title or author:")
    results = library.search_books("the")
    for book in results:
        print(f"  {book}")
    
    # Check out a book
    print("\n4. Checking out '1984':")
    library.check_out_book("978-0-452-28423-4")
    library.display_all_books()
    
    # Return a book
    print("\n5. Returning '1984':")
    library.return_book("978-0-452-28423-4")
    library.display_all_books()
    
    # Remove a book
    print("\n6. Removing 'Pride and Prejudice':")
    library.remove_book("978-0-14-143951-6")
    library.display_all_books()

if __name__ == "__main__":
    main()