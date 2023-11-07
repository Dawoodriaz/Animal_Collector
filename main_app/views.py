from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Animal , Country
from django.views.generic.edit import CreateView , UpdateView, DeleteView
from django.views.generic import ListView,DetailView
from .forms import FeedingForm


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# class Animals:  
#   def __init__(self, animal, eat, description, age,price):
#     self.animal = animal
#     self.eat = eat
#     self.description = description
#     self.age = age
#     self.price = price

# animals = [
#   Animals('Giraffe', 'Herbivores', 'Tall', 3,30000 ),
#   Animals('Elephant', 'Herbivores', 'Thick with a trunck', 4,5000),
#   Animals('Tiger', 'carnivores', 'Fierce', 4,10000)
# ]



class AnimalCreate(LoginRequiredMixin,CreateView):
  model= Animal
  fields ='__all__'
  
  
class AnimalUpdate(LoginRequiredMixin,UpdateView):
  model=Animal
  fields= '__all__'

class AnimalDelete(LoginRequiredMixin,DeleteView):
  model=Animal
  success_url ='/animals/'

# Create your views here.
def home(request):
  return render(request, 'index.html')


def about(request):
  return render(request,'about.html')



@login_required
# Add new view
def animals_index(request):
  animals =Animal.objects.all()
  return render(request, 'animals/index.html', { 'animals': animals })



# def animals_details(request,animal.id):
#   ani=

@login_required
def animals_details(request,animal_id):
  #select * from 'main_app_animal' WHERE id=animal_id
  animal = Animal.objects.get(id=animal_id)
  feeding_form = FeedingForm()
  countries_animal_doesnt_have= Country.objects.exclude(id__in = animal.countries.all().values_list('id'))
  return render(request, 'animals/detail.html', {'animal':animal , 'feeding_form': feeding_form , 'countries':countries_animal_doesnt_have })

@login_required
def add_feeding(request, animal_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_Feeding = form.save(commit=False)
    new_Feeding.animal_id = animal_id
    new_Feeding.save()
  return redirect('detail',animal_id = animal_id)

#CBV'c for countries CRUD operation


class CountryList(LoginRequiredMixin,ListView):
  model= Country
  
  
class CountryDetail(LoginRequiredMixin,DetailView):
  model= Country
  
  
class CountryCreate(LoginRequiredMixin,CreateView):
  model =Country
  fields = ['name']
  
  
class CountryUpdate(LoginRequiredMixin,UpdateView):
  model = Country
  fields = ['name']
  
class CountryDelete(LoginRequiredMixin,DeleteView):
  model =Country
  success_url = '/countries/' 
  
  
 

# 

def assoc_country(request, animal_id, country_id):
    animal = Animal.objects.get(id=animal_id)
    country = Country.objects.get(id=country_id)
    animal.countries.add(country)
    return redirect('detail', animal_id=animal_id)

def unassoc_country(request, animal_id, country_id):
    animal = Animal.objects.get(id=animal_id)
    country = Country.objects.get(id=country_id)
    animal.countries.remove(country)
    return redirect('detail', animal_id=animal_id)

# sign up

def signup(request):
  error_message=''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user= form.save()
      login(request,user)
      return redirect('index')
    else:
      error_message='invalid Signup-- Please TRy again Later', form.error_messages
      
  form = UserCreationForm()
  context = {'form':form , 'error_message':error_message}
  return render(request, 'registration/signup.html',context)
