from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

from mysite.core import views as core_views


urlpatterns = [
    url(r'^$', core_views.home, name='home'),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^signup/$', core_views.signup, name='signup'),
##django 3.1.13
##automatically maps the below mentioned URLs.
##accounts/ login/ [name='login']
##accounts/ logout/ [name='logout']
##accounts/ password_change/ [name='password_change']
##accounts/ password_change/done/ [name='password_change_done']
##accounts/ password_reset/ [name='password_reset']
##accounts/ password_reset/done/ [name='password_reset_done']
##accounts/ reset/<uidb64>/<token>/ [name='password_reset_confirm']
##accounts/ reset/done/ [name='password_reset_complete']
    
##    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
##    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
##    url(r'^signup/$', core_views.signup, name='signup'),
]
