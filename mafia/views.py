from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

# rooms

def lobby(request):
    return HttpResponse("HOME")


def create_room(request):
    return HttpResponse("not implemented")


def add_room(request):
    return HttpResponse("not implemented")


def enter_room(request):
    return HttpResponse("not implemented")


# messaging

def send_message(request):
    """
    client adds a message to the server.
    should contain error checking as to whether the message is
    a legal message (recipient exists)
    :param request:
    :return:
    """
    pass

def check_data(request):
    """
    This allows for the client to check for new/changed data
    on the server and update itself accordingly (since http
    is a pull protocol)

    :param request:
    :return:
    """
    pass