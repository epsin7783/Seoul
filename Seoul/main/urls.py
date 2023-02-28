from django.urls import path, include
from . import views

urlpatterns = [
        path("main", views.MainView.as_view(), name="main" ),
        path("googleapitest", views.GoogleView.as_view(), name="googleapitest" ),
        path("", views.TestView.as_view(), name="test" ),
    ]

