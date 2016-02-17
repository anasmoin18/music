from django.conf.urls import include, url
from django.contrib import admin
from gaana import views

urlpatterns = [
    url(r'^sign-up/$', views.sign_up, name='sign_up'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout_page'),
    url(r'^home/$', views.home, name='home'),
    url(r'^admin/', include(admin.site.urls)),
]