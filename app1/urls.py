from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.views import generic
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = "app1"

urlpatterns = [
    path('Masterspage/',views.MasterListView.as_view(), name='Masterspage'),
]
