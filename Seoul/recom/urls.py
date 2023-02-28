from django.urls.conf import path
from recom import views

urlpatterns = [
    path( "recom", views.RecomView.as_view(), name="recom" ),
    
    ]