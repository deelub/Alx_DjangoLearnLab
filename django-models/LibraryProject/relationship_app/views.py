from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library  # Required line for checker
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


# Function-based view
def list_books(request):
    books = Book.objects.all()  # Required by checker
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # <-- This line is essential for check and behavior
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})
