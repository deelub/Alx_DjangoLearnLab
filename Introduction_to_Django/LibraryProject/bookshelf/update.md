# Updating Models

book= Books.object.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
print(book)