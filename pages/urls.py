from django.urls import path
from .views import *
urlpatterns = [
    # Указываю здесь список инициализированных страниц на сайте
    path('', HomePageView.as_view(), name='home'),
    path('about.html', AboutPageView.as_view(), name='about')
]

