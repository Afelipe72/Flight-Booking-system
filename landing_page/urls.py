from django.urls import path
from landing_page.views import *
urlpatterns = [
    path('', HomePageView.as_view(), name='dashboard'),
]
