#! a data class is a class that is designed to only hold data values. They aren't different from regular classes, but they usually don't have any other methods. They are typically used to store information

from dataclasses import dataclass , field
import random

def genrator_number():
    count = 1001
    while True :
        yield count
        count += 1

gen = genrator_number()
def genrator():
    return f"{chr(random.choice(range(ord('a'), ord('z'))))}"

@dataclass(kw_only = True,frozen= True)#frozen to make constant objects
class Person:
    Name : str
    Age : int
    active : bool = True
    email : list[str] = field(default_factory = list)
    Id : str = field(default_factory= genrator,init= False)




P1 = Person(Name ="Ashy",Age = 19,email=["ashuthakur07@gmail.com"])
print(P1)

# Books And Librarys

import random

from dataclasses import dataclass, field

def genrate_string():
    return f"ISO:{random.randint(1,100)}"

@dataclass(kw_only = True)
class Book:
    title: str
    author: str
    isbn: str = field(default_factory=genrate_string)
    published_year: int  
    available: bool

    def __str__(self) -> str:
        return f"{self.title} written by {self.author}"

@dataclass
class Library:
    name: str
    address: str
    books: list[Book] = field(default_factory=list)

    def add_book(self, book: Book) -> Book:
        self.books.append(book)
        return book
    
    def remove_book(self, book: Book) -> None:
        if book in self.books:
            self.books.remove(book)
        else:
            print("Book doesn't exist in the library.")

    def find_book(self, isbn: str) -> Book:
        for book in self.books:
            if book.isbn == isbn:
                return book
        print("Book doesn't exist in the library.")
        return None 

if __name__ == "__main__":
   
    library = Library(name="Central Library", address="123 Main St.")

    
    book1 = Book(title="Python Programming", author="Guido van Rossum", isbn="ISO:42", published_year=2020, available=True)
    book2 = Book(title="Java Basics", author="James Gosling", published_year=2018, available=False)

    library.add_book(book1)
    library.add_book(book2)

  
    library.remove_book(book2)

    
    found_book = library.find_book("ISO:42")
    if found_book:
        print("Found book:", found_book)
