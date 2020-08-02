from django.urls import path
from .views import DateListView

app_name = 'data'

urlpatterns = [
    path('data/', DateListView.as_view()),
]