from django.urls import path
from .views import formTransactions , filter
urlpatterns = [
    path('', formTransactions),
    path('filter/<str:store>', filter, name= "filter")
]