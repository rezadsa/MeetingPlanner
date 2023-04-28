from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from datetime import datetime

from meetings.models import Meeting  # type:ignore


def welcome(request):
    return render(request, 'website/home.html',
                  {'meetings': Meeting.objects.all()})


def date(request):
    return HttpResponse(f'This page has served at {str(datetime.now())}')


def about(request):
    return HttpResponse('my name is reza safarkhani')
