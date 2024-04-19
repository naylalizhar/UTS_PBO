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

    def add_member(self, member):
        self.members.append(member)

    def add_librarian(self, librarian):
        self.librarian = librarian

    def display_books(self):
        if self.books:
            print("Books in Library:")
            for book in self.books:
                print(f"Book ID: {book.book_id}, Title: {book.title}, Author: {book.author}")
        else:
            print("No books available in the library.")

    def display_members(self):
        if self.members:
            print("Library Members:")
            for member in self.members:
                print(f"Member ID: {member.member_id}, Name: {member.name}, Address: {member.address}")
        else:
            print("No members registered in the library.")

    def display_transactions(self):
        if self.transactions:
            print("Library Transactions:")
            for transaction in self.transactions:
                print(f"Transaction ID: {transaction.transaction_id}, Book ID: {transaction.book_id}, Member ID: {transaction.member_id}, Borrow Date: {transaction.borrow_date}, Return Date: {transaction.return_date}, Status: {transaction.status}")
        else:
            print("No transactions recorded in the library.")
