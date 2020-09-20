from models.models import Book

if __name__ == '__main__':  # pragma: no cove
    book = Book()
    book.author = 'Tim Cook'
    book.title = 'iPhone. My story'
    book.save()
    print(book.id)

    book.author = 'Steve Jobs'
    book.save()
    print(book.author)

    book = Book(1)
    print(book.title)
    print(book.author)
