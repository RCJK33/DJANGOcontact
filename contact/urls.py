from django.urls import path, include
from contact.views import contact

urlpatterns = [
    path('', contact, name='contact' ),
]