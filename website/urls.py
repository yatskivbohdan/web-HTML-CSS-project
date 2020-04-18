from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('html_home', views.html_home, name='html_home'),
    path('html_home/tags', views.tags, name='tags'),
    path('html_home/attributes', views.attributes, name='attributes'),
    path('html_home/forms', views.forms, name='forms'),
    path('html_home/meta', views.meta, name='meta'),
    path('html_home/html_resources', views.html_resources, name='html_resources'),
    path('css_home', views.css_home, name='css_home'),
    path('css_home/box_model', views.box_model, name='box_model'),
    path('css_home/margin', views.margin, name='margin'),
    path('css_home/display', views.display, name='display'),
    path('css_home/flexbox', views.flexbox, name='flexbox'),
    path('css_home/css_resources', views.css_resources, name='css_resources'),

]