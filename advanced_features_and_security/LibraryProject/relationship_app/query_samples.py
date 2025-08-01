import os
import django

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_models.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def run_queries():
    # 1. Query all books by a specific author
    author_name = "Jane Austen"
try:
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)
    print(f"\nBooks by {author_name}:")
    for book in books:
        print(f"- {book.title}")
except Author.DoesNotExist:
    print(f"\nAuthor '{author_name}' not found.")

    # 2. List all books in a library
    library_name = "Central Library"
    try:
        library = Library.objects.get(name=library_name)
        print(f"\nBooks in {library_name}:")
        for book in library.books.all():
            print(f"- {book.title}")
    except Library.DoesNotExist:
        print(f"\nLibrary '{library_name}' does not exist.")

    # 3. Retrieve the librarian for a library
    try:
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library=library)
        print(f"\nLibrarian of {library_name}: {librarian.name}")
    except Library.DoesNotExist:
        print(f"\nLibrary '{library_name}' not found.")
    except Librarian.DoesNotExist:
        print(f"\nNo librarian assigned to {library_name}.")

if __name__ == "__main__":
    run_queries()