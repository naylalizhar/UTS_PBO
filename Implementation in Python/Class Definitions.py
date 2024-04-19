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
