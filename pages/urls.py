from django.urls import path
from .views import HomePageView
urlpatterns = [
    # Представил объект класса с помощью as_view()
    path('', HomePageView.as_view(), name='home')
]

