from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from .models import Book
from .serializers import BookSerializer

# Optional: public read-only endpoint
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Full CRUD + auth required
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
