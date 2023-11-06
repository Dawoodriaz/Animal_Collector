from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Animal , Toy
from django.views.generic.edit import CreateView , UpdateView, DeleteView
from django.views.generic import ListView,DetailView
from .forms import FeedingForm

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



class AnimalCreate(CreateView):
  model= Animal
  fields ='__all__'
  
  
class AnimalUpdate(UpdateView):
  model=Animal
  fields= '__all__'

class AnimalDelete(DeleteView):
  model=Animal
  success_url ='/animals/'

# Create your views here.
def home(request):
  return render(request, 'index.html')


def about(request):
  return render(request,'about.html')



# Add new view
def animals_index(request):
  animals =Animal.objects.all()
  return render(request, 'animals/index.html', { 'animals': animals })



# def animals_details(request,animal.id):
#   ani=


def animals_details(request,animal_id):
  #select * from 'main_app_animal' WHERE id=animal_id
  animal = Animal.objects.get(id=animal_id)
  feeding_form = FeedingForm()
  toys_animal_doesnt_have= Toy.objects.exclude(id__in = animal.toys.all().values_list('id'))
  return render(request, 'animals/detail.html', {'animal':animal , 'feeding_form': feeding_form , 'toys':toys_animal_doesnt_have })


def add_feeding(request, animal_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_Feeding = form.save(commit=False)
    new_Feeding.animal_id = animal_id
    new_Feeding.save()
  return redirect('detail',animal_id = animal_id)

#CBV'c for toys CRUD operation


class ToyList(ListView):
  model= Toy
  
  
class ToyDetail(DetailView):
  model= Toy
  
  
class ToyCreate(CreateView):
  model =Toy
  fields = ['name','color']
  
  
class ToyUpdate(UpdateView):
  model = Toy
  fields = ['name','color']
  
class ToyDelete(DeleteView):
  model =Toy
  success_url = '/toys/' 
  
  
 

# 

def assoc_toy(request, animal_id, toy_id):
    animal = Animal.objects.get(id=animal_id)
    toy = Toy.objects.get(id=toy_id)
    animal.toys.add(toy)
    return redirect('detail', animal_id=animal_id)

def unassoc_toy(request, animal_id, toy_id):
    animal = Animal.objects.get(id=animal_id)
    toy = Toy.objects.get(id=toy_id)
    animal.toys.remove(toy)
    return redirect('detail', animal_id=animal_id)

