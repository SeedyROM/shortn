from django.conf.urls import url

from urls import views


urlpatterns = [
    url(r'^$', views.new_url, name='new_url'),
    url(r'^(?P<tiny_url>[a-zA-Z0-9]{9})$', views.goto_url, name='goto_url'),
    url(r'^c$', views.create_url, name='create_url'),
    url(r'^v/(?P<tiny_url>[a-zA-Z0-9]{9})$', views.view_url, name='view_url'),
]
