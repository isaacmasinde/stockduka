from django.urls import path
from .views import *
urlpatterns = [
	path('', items, name='items'),
	path('categories/', categories, name='categories'),
	path('users/', users, name='users'),
	path('brands/', brands, name='brands'),
]