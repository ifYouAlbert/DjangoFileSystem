from django.urls import path
from .views import home, work

urlpatterns = [
    path('', home, name='home'),
    path('work/', work, name='work'),
]