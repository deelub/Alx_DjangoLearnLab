book=  book.objects.get(title="Nineteen Eighty-Four")
book.delete()
Book.objects.all()