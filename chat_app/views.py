
from django.shortcuts import render , redirect
from .models import Room , Message

# Create your views here.

def Homeview(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        room = request.POST.get('room')
        try :
            existing_room = Room.objects.get(room_name__icontains=room)
        except Room.DoesNotExist:
            r = Room.objects.create(room_name=room)    
        return redirect('Roomview', room_name=room, username=username)
    return render(request, 'home.html')

def Roomview(request, room_name, username):
    existing_room = Room.objects.get(room_name__icontains=room_name)
    get_messages = Message.objects.filter(room_id=existing_room)
    context = {
        'room_name': room_name,
        'username': username,
        'messages': get_messages
    }
    return render(request, 'room.html', context)