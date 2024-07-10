from dataclasses import dataclass, field
import datetime
import copy

@dataclass(frozen=True)
class User:
    username: str
    password: str
    email_id: str 
    phone_number: str
    address: str
    _book_borrowed: list[str] = field(default_factory=list, init=False)
    _book_borrowed_date: dict = field(default_factory=dict, init=False)

    def update_phone_number(self, password, phone_number):
        if password and password == self.password:
            # Use object.__setattr__ to bypass the frozen attribute restriction
            object.__setattr__(self, 'phone_number', phone_number)
            return True
        return False

    def _add_books(self, books):
        for book in books:
            self._book_borrowed.append(book)
            today = datetime.datetime.today()
            formatted_date = today.strftime("%Y-%m-%d")
            self._book_borrowed_date[book] = formatted_date

    def user_view(self):
        return (f"Username: {self.username}\nEmail ID: {self.email_id}\nPhone Number: {self.phone_number}\n"
                f"Address: {self.address}\nBorrowed Books: {self._book_borrowed}\n"
                f"Borrowed Date: {self._book_borrowed_date}")

class Library:
    library_name = "Readers & Learners"
    library_code = "B1245LC"
    library_address = "Vijaynagar, Indore, 452014"
    library_phone_number = "0731-2345678"
    library_email_id = "library@readersandlearners.com"

    def __init__(self, **books_with_quantities):
        self.__total_books = {key: value for key, value in books_with_quantities.items()}
        self.available_books = copy.deepcopy(self.__total_books)
        self.borrowed_books = {}
        self._total_users = []

    def show(self):
        print("Library Name:", self.library_name)
        print("Here is the books list-----:")
        for book, quantity in self.available_books.items():
            print(f"{book}: {quantity}")

    def borrow_book(self, book_name):
        if book_name in self.available_books and self.available_books[book_name] > 0:
            username = input("Please enter your username: ").strip()
            for obj in self._total_users:
                if obj.username == username:
                    obj._add_books([book_name])
                    if self.borrowed_books.get(book_name):
                        self.borrowed_books[book_name].append(username)
                    else:
                        self.borrowed_books[book_name] = [username]

                    self.available_books[book_name] -= 1
                    print("Book borrowed successfully")
                    return
            print("User not found")
        else:
            print("Book is not available or out of stock")

    def add_user(self):
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        phone_regex = r'^[0-9]{10}$'
        username = input("Please enter your username: ")

        if not any(user.username == username for user in self._total_users):
            password = input("Please enter your password: ")
            email_id = input("Please enter your email ID: ")
            if Library.__varification_for_data(email_id, email_regex):
                phone_number = input("Please enter your phone number: ")
                if Library.__varification_for_data(phone_number, phone_regex):
                    address = input("Enter address: ")
                    obj = User(username=username, password=password, email_id=email_id, phone_number=phone_number, address=address)
                    self._total_users.append(obj)
                    print("User added successfully")
                else:
                    print("Please enter a valid phone number")
            else:
                print("Invalid Email ID")
        else:
            print("Username already exists")

    @staticmethod
    def __varification_for_data(data, pattern):
        import re
        return bool(re.match(pattern, data))

    def add_books(self, **kwargs):
        for book_name, quantity in kwargs.items():
            if book_name in self.available_books:
                self.available_books[book_name] += quantity
            else:
                self.available_books[book_name] = quantity
        print("Books added successfully")

    def info(self):
        welcome_string = (f"Welcome to our Library {self.library_name}\n"
                          f"We have around {len(self.__total_books)} books in our collection\n"
                          f"Around {len(self._total_users)} users are connected with us\n")
        print(welcome_string)

    def return_book(self, username, book_name):
        for obj in self._total_users:
            if obj.username == username:
                if book_name in obj._book_borrowed:
                    obj._book_borrowed.remove(book_name)
                    del obj._book_borrowed_date[book_name]
                    self.available_books[book_name] += 1
                    if username in self.borrowed_books[book_name]:
                        self.borrowed_books[book_name].remove(username)
                    print("Book returned successfully")
                    return
        print("Book return failed")