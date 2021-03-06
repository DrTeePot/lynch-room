from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from entry.models import UserProfile
from mafia.forms import RoomForm, RulesForm, RoleForm, StoryForm, MessageForm, JoinRoomForm

# Create your views here.

# rooms
from mafia.models import Room


@login_required()
def lobby(request):
    # TODO messaging framework
    return render(request,
                  'mafia/lobby.html',
        {
            #TODO List of games user is in
        })


@login_required()
def create(request):

    room_form = RoomForm()
    rule_form = RulesForm()

    # Render the template depending on the context.
    return render(request,
                  'mafia/create.html',
                  {'room_form': room_form, 'rule_form': rule_form})

@login_required()
def create_rule(request):
    # Set to False initially. Code changes value to True when creation succeeds.
    created = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        rule_form = RulesForm(data=request.POST)

        if rule_form.is_valid():
            rules = rule_form.save()

            rules.save()

            return JsonResponse({'response': 'Rule created'})

        else:
            print rule_form.errors

    return JsonResponse({'response': 'Errors were found'})

@login_required()
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

            return JsonResponse({'response': 'Room created'})

        else:
            print room_form.errors

    return JsonResponse({'response': 'Errors were found'})


@login_required()
def add_room(request):
    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        room_form = JoinRoomForm(data=request.POST)

        room_name = request.POST['name']
        room_pass = request.POST['password']

        try:
            room = Room.objects.get(name=room_name)
            if room.password == room_pass:
                room.add_user(user=UserProfile.objects.get(user=request.user))
                return HttpResponseRedirect(redirect_to='/play/game/')  # TODO change to game id or name
        except (Room.DoesNotExist, Room.MultipleObjectsReturned):
            print "Room ", room_name, "Does not exist"
            return JsonResponse({'response': 'Room/pass incorrect'})

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


@login_required()
def enter_room(request):
    return render(request,
                  'mafia/gameroom.html',
        {})

@login_required()
def vote(request):
    """
    request should contain an ajax request in JSON form
    returns info on revote, first vote, failure, etc
    :param request:
    :return:
    """
    pass


# messaging
@login_required()
def send_message(request):
    """
    client adds a message to the server.
    should contain error checking as to whether the message is
    a legal message (recipient exists)
    :param request:
    :return:
    """
    pass

@login_required()
def check_data(request):
    """
    This allows for the client to check for new/changed data
    on the server and update itself accordingly (since http
    is a pull protocol)

    :param request:
    :return:
    """
    pass