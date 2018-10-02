import time


class Book(object):
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return "[Title: {}, Author: {}, Pages:{}]".format(self.title, self.author, self.pages)

    def __len__(self):
        return self.pages

    def __del__(self):
        print("""
        __del__ is like a destructor
        Once all ref to this object is deleted it will be called
        """)


b = Book("Python", "jose", 101)
print(b)
print("Book Length: {}".format(len(b)))

b = 1
print("Waiting if b is deleted")
time.sleep(4)
print(__name__)
