from django.urls import path

from .views import index, about, service, contact

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('services/', service, name='service'),
    path('contact/', contact, name='contact'),

]
