from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, question_id):
    return HttpResponse("You're looking at question {}".format(question_id))

def vote(request, question_id):
    return HttpResponse("You're voting on question {}".format(question_id))
