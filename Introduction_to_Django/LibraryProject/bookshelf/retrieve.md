# Retrieving Book Instance

from library.models import Book
book= Book.object.get(title="1984")
print(book.title, book.author, book.publication_year)