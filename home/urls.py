from . import views
from django.urls import path

urlpatterns = [
    path('home/', views.home_page.as_view(), name='home'),
]