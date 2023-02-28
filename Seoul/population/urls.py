from django.urls.conf import path
from django.views.generic.base import TemplateView
from population import views

urlpatterns = [
    path( "", views.PopulationMainView.as_view(), name="population" ),
    ]