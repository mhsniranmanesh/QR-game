from django.conf.urls import url
from game import views


urlpatterns = [
    url(r'(?P<barcode_id>[0-9]+)/(?P<phone_number>[0-9]+)/$', views.submit, name='submit'),
    url(r'(?P<barcode_id>[0-9]+)/$', views.index, name='index'),
]