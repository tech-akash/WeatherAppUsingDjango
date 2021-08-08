from django import forms
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .models import City
from .forms import Addcity
# Create your views here.

def city_view(request):
    form =Addcity(request.POST or None)
    # form.clean()
    
    
    if form.is_valid():
        form.save()
        form=Addcity()
        return HttpResponseRedirect('/')
        
       
    cities=City.objects.all()
    city1=[]
    for city in cities:
      temp=city.cityName[0].upper()+city.cityName[1:].lower()
      city1.append(temp)
    cityid=[]
    for temp in cities:
        cityid.append(temp.id)
    
    cities=set(cities)
    print(len(cities))
    cities=list(cities)
    city1=set(city1)
    context={
        'form': form,
        'cities':cities,
        'cityid':cityid
    }
    return render(request,'citytemp.html',context)
def delete(request, id):
    print(id)
    stock_to_delete = get_object_or_404(City, id=id).delete()
    return redirect(city_view)