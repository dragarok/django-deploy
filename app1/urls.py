from django.conf.urls import url
from app1 import views

app_name = 'app1'
# made after making the app and on second step for app to have own urls.py
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'signup/', views.signup_view, name='signup'),
    url(r'^other/$', views.other, name='other'),
    url(r'^user_login/$', views.user_login, name='user_login'),
]
