from django.urls import path
from .views import *
urlpatterns = [
	path('', profile, name='profile'),
	path('addon/', addon, name='addon'),
	path('remove/', remove, name='remove'),
	path('orders/', orders, name='orders'),
	path('details/', orders, name='details'),
	path('complete/', complete, name='complete'),
]