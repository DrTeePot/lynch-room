from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    """
    This needs to check whether user is logged in.
    If logged in, display info on current games.
    Display info.

    :return:
    """
    return HttpResponse("HOME")