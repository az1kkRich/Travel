from django.urls import path
from .views import Index, Contact, new_detail, NewsCreateView

urlpatterns = [
    path('', Index.as_view(), name='home'),
    path('news/', NewsCreateView.as_view(), name='news'),
    path('contact/', Contact, name='contact'),
    path('new/<slug:newSlug>/', new_detail.as_view(), name='new_detail'),
]