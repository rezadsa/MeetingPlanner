from django.shortcuts import render,get_object_or_404,redirect

from .models import Meeting,Room
from .form import MeetingForm

# Create your views here.



def details(request,id):
    # meeting=Meeting.objects.get(pk=id)
    meeting=get_object_or_404(Meeting,pk=id)
    return render(request,'meetings/detail.html',{'meeting':meeting})

def rooms_list(request):
    return render(request,'meetings/rooms_list.html',
                  {'rooms':Room.objects.all()})

# MeetingForm=modelform_factory(Meeting,exclude=[])

def form(request):
    if request.method=='POST':
        form=MeetingForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=MeetingForm()

        
    return render(request,'meetings/form.html',{'form':form})