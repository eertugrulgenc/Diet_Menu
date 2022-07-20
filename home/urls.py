from django.urls import re_path as url
from .views import logout_view

app_name = 'home'

urlpatterns = [
    url('logout/', logout_view, name='logout')
]