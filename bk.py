class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    def get_descriptive(self):
        print(f"{self.title} written by {self.author} in {self.year}")        
        
favorite_book = Book("kaleidar","Dolatabadi", 1946 )
favorite_book.get_descriptive()
favorite_book02 = Book("Desiree", "Selinco", 1891)
favorite_book02.get_descriptive()
        