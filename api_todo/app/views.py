from app.models import Todo
from app.serializers import TodoSerializer

from rest_framework import viewsets

#criando métodos get,post,delete,put 

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
