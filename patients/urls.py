from django.urls import re_path as url
from .views import login_view

app_name = 'patients'

urlpatterns = [
    url('login/', login_view, name='login')
]