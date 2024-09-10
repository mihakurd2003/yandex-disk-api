from django.urls import path
from yandex_disk import views

urlpatterns = [
    path('', views.files_list, name='files_list'),
]
