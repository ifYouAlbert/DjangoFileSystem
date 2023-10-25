from django.urls import path
from .views import page, delete

urlpatterns = [
    path('', page, name='files'),
    path('delete', delete, name='delete')

]
