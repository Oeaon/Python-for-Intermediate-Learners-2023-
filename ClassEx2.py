class Book:
    def __init__(self,name,pages):
        self.name=name
        self.pages=pages

    def __add__(self, other):
        return self.pages + other.pages
    
bookOne= Book("The Godfather",600)
bookTwo= Book("The silence of the lumbs", 400)

print(bookOne + bookTwo)