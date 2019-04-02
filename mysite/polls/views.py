from django.shortcuts import render
from .models import CreatorOneToOne, CreationOneToOne, MTOCreation, OTMCreator, MTMCreation, MTMCreator
# Create your views here.
from django.http import HttpResponse


def index(request):
    # mm_objects = MTMCreator.objects.all().first().mtmcreation_set.all()
    # mcrotrs = MTMCreation.objects.all().first().mtm_creator.all()
    return HttpResponse("Hello, world. You're at the polls index.")
