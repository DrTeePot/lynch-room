from django.http import HttpResponse
from django.shortcuts import render
from mafia.forms import RoomForm, RulesForm, RoleForm, StoryForm, MessageForm


# Create your views here.

# rooms

def lobby(request):
    return HttpResponse("HOME")


def create_room(request):
    # Set to False initially. Code changes value to True when creation succeeds.
    created = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        room_form = RoomForm(data=request.POST)

        if room_form.is_valid():
            room = room_form.save()

            room.save()

            # Update our variable to tell the template creation was successful.
            created = True

        else:
            print room_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        room_form = RoomForm()

    # Render the template depending on the context.
    return render(request,
                  'mafia/create_room.html',
                  {'room_form': room_form, 'created': created})


def add_room(request):
    return HttpResponse("not implemented")


def enter_room(request):
    return render(request,
                  'gameroom.html',
        {})


def vote(request):
    """
    request should contain an ajax request in JSON form
    returns info on revote, first vote, failure, etc
    :param request:
    :return:
    """
    pass


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