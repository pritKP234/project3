from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def first_string_response(request):
    return HttpResponse('This is my 1st string')

def second_string_response(request):
    return HttpResponse('This is my 2nd string')

def third_string_response(request):
    return HttpResponse('This is my 3rd string')