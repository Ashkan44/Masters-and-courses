from django.shortcuts import render
from django.views import generic
from . import models


# Create your views here.

class MasterListView(generic.ListView):
    model = models.Master