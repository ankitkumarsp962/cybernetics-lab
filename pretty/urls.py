from django.urls import path
from pretty.views import prettify_number


urlpatterns = [
    path("numbers/", prettify_number, name="prettfy_number"),
]
