from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.Contact, name='contact')

    # {Changed the name of the function from contact to Contact because of the function we changed}
]
