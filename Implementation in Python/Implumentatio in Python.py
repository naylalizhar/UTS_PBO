class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True

class Member:
    def __init__(self, member_id, name, address, card_number):
        self.member_id = member_id
        self.name = name
        self.address = address
        self.card_number = card_number

class Librarian:
    def __init__(self, librarian_id, name):
        self.librarian_id = librarian_id
        self.name = name

class Transaction:
    def __init__(self, transaction_id, book_id, member_id, borrow_date, return_date=None):
        self.transaction_id = transaction_id
        self.book_id = book_id
        self.member_id = member_id
        self.borrow_date = borrow_date
        self.return_date = return_date
        self.status = "On Loan" if return_date is None else "Returned"

class LibrarySystem:
    def __init__(self):
        self.books = []
        self.members = []
        self.transactions = []
        self.librarian = None

    def add_book(self, book):
        self.books.append(book)

    def search_book(self, keyword):
        results = []
        for book in self.books:
            if keyword.lower() in book.title.lower() or keyword.lower() in book.author.lower():
                results.append(book)
        return results

    def borrow_book(self, book_id, member_id, borrow_date):
        book = next((b for b in self.books if b.book_id == book_id), None)
        if book is not None and book.available:
            transaction_id = len(self.transactions) + 1
            transaction = Transaction(transaction_id, book_id, member_id, borrow_date)
            self.transactions.append(transaction)
            book.available = False
            return True
        else:
            return False

    def return_book(self, transaction_id, return_date):
        transaction = next((t for t in self.transactions if t.transaction_id == transaction_id), None)
        if transaction is not None:
            transaction.return_date = return_date
            transaction.status = "Returned"
            book = next((b for b in self.books if b.book_id == transaction.book_id), None)
            if book is not None:
                book.available = True
            return True
        else:
            return False

# Contoh penggunaan sistem perpustakaan
if __name__ == "__main__":
    # Inisialisasi sistem perpustakaan
    library_system = LibrarySystem()

    # Tambahkan beberapa buku ke dalam sistem
    book1 = Book(1, "Python Programming", "John Smith")
    book2 = Book(2, "Data Science Handbook", "Jane Doe")
    library_system.add_book(book1)
    library_system.add_book(book2)

    # Cari buku berdasarkan kata kunci
    search_results = library_system.search_book("Python")
    print("Search Results:")
    for book in search_results:
        print(f"- {book.title} by {book.author}")

    # Simulasikan peminjaman buku
    borrow_date = "2024-04-20"
    member_id = 1
    success = library_system.borrow_book(book1.book_id, member_id, borrow_date)
    if success:
        print("Book borrowed successfully!")
    else:
        print("Failed to borrow book. It may not be available.")

    # Simulasikan pengembalian buku
    return_date = "2024-04-25"
    transaction_id = 1  # Misalnya, ID transaksi pertama
    success = library_system.return_book(transaction_id, return_date)
    if success:
        print("Book returned successfully!")
    else:
        print("Failed to return book. Invalid transaction ID.")
