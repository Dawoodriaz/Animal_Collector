from django.shortcuts import render
from django.http import HttpResponse



class Animals:  
  def __init__(self, animal, eat, description, age,price):
    self.animal = animal
    self.eat = eat
    self.description = description
    self.age = age
    self.price = price

animals = [
  Animals('Giraffe', 'Herbivores', 'Tall', 3,30000 ),
  Animals('Elephant', 'Herbivores', 'Thick with a trunck', 4,5000),
  Animals('Tiger', 'carnivores', 'Fierce', 4,10000)
]






# Create your views here.
def home(request):
  return render(request, 'index.html')


def about(request):
  return render(request,'about.html')



# Add new view
def animals_index(request):
  return render(request, 'animals/index.html', { 'animals': animals })
