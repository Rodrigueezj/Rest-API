from django.urls import path, include 
from . import views
from rest_framework import routers #allows to make get/post requests

router = routers.DefaultRouter()
router.register('reports', views.ReportView)

urlpatterns = [
    path('', include(router.urls))
]