from django.urls import path
from bases.views import index, type, offers, functional, contact, open_csv

urlpatterns = [
    path('', index),
    path('type/', type, name="type"),
    path('offers/', offers, name="offers"),
    path('functional/', functional, name="functional"),
    path('contact/', contact, name="contact"),
    path('functional/api/csv/', open_csv, name="open_csv"),

]