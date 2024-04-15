from django.urls import path
from .views import get_reviews


app_name = 'techorders'

urlpatterns = [
    path('reviews/', view=get_reviews, name="reviews")
]