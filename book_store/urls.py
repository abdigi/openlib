from django.urls import path
from . import views

urlpatterns=[
  path('',views.index),
  path('login',views.logins,name="login"),
  path('register',views.register),
  path('bookinsert',views.bookinsert)
]