from django.conf.urls import url, include
from .views import home, contact

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^contact/$', contact, name='contact')
]