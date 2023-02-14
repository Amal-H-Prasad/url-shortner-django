from django.shortcuts import render
from django.http import HttpResponse
import uuid
from .models import Url

def index(request):
    return render(request, "index.html")

def create(request):
   if request.method == 'POST':
       link = request.POST['link']
       uid = str(uuid.uuid4())[:5]
       new_Url=Url(link=link,uuid=uid)
       new_Url.save()
       return HttpResponse(uid)