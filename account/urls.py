from django.urls import path
from . import views
urlpatterns = [
    path('login/', views.login, name='Login'),
    path('register/', views.register, name='signup'),
    path('logout/', views.logout, name='Logout'),
]
