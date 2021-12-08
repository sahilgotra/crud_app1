from django.shortcuts import render, redirect
import myapp

from myapp.models import registration
from .forms import regForm
# Create your views here.
def index(request):
  form = regForm()
  data = registration.objects.all()
  if request.method == 'POST':
    form = regForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      return redirect('/')
  return render(request, 'myapp/index.html', {'form':form, 'data':data})


def showform(request, id):
  data = registration.objects.filter(id=id)
  return render(request, 'myapp/showform.html', {'data':data})

def edit(request, id):
  data = registration.objects.get(id=id)
  form = regForm(instance=data)
  if request.method == "POST":
    data = registration.objects.get(id=id)
    form = regForm(request.POST, instance=data)
    if form.is_valid():
      form.save()
      return redirect('/')
  return render(request, 'myapp/edit.html', {'data':data, 'form':form})

# def update(request, id):
#   form = regForm(instance=data)
#   if request.method == "POST":
#     data = registration.objects.get(id=id)
#     form = regForm(request.POST, instance=data)
#     if form.is_valid():
#       form.save()
#       return redirect('/')
#   return render(request, 'myapp/edit.html', {'form':form,'data':data})

 
def delete(request, id):
  data = registration.objects.get(id=id)
  data.delete()
  return redirect('/')
