
from django.shortcuts import render

# Create your views here.

from django.shortcuts import redirect, render
from .models import *
# Create your views here.
def index(request):
    item = contct.objects.all()
    return render(request,'index.html',{'data' : item})
def profile(request,pk):
    item = contct.objects.get(id = pk)
    return render(request,'profile.html',{'data': item})
def register(request):
    if request.method == 'POST':
        new_contact = contct(
            name = request.POST['fullname'],
            phone = request.POST['phone']
        )
        new_contact.save()
        return redirect('/')
    return render(request,'register.html')
def edit(request,pk):
    item = contct.objects.get(id = pk)
    if request.method == 'POST':
        # print()
        item.name = request.POST.get('fullname')
        item.phone = request.POST.get('phone')
        item.save()
        return redirect('/profile/'+str(item.id))
    return render(request,'edit.html',{'data':item})

def delete(request,pk):
    item = contct.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('/')
    return render(request,'delete.html',{'data':item})
