from django.shortcuts import render
from django.utils.safestring import mark_safe
import json

def index(request):
    return render(request, 'draw/index.html', {})
def index2(request):
    return render(request, 'draw/index2.html')
  
def index3(request):
    return render(request, 'draw/index3.html')

# def room(request, room_name):
    # return render(request, 'draw/room.html', {
       # 'room_name_json': mark_safe(json.dumps(room_name))
    # }) 