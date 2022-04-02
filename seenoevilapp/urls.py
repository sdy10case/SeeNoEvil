from .import views
from django.urls import  path
app_name = 'seenoevilapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('<str:url>', views.get_content_list, name='get_content_list'),
]
