from django.urls import path
from web.views import index, about


urlpatterns = [
    path("",index),
    path("about/",about)
]