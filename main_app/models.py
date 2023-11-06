from django.db import models
from django.urls import reverse
from datetime import date

#Tuple
MEALS= (('B','BREAKFAST'),('L','LUNCH'),('D','DINNER'))
# Create your models here.


class Toy(models.Model):
    name= models.CharField(max_length=50)
    color = models.CharField(max_length=20)
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse ('toys_detail', kwargs={'pk':self.id})

class Animal(models.Model):
    animal=models.CharField(max_length=100,  default="")
    eat=models.CharField(max_length=100,  default="")
    description=models.CharField(max_length=100,  default="")
    age=models.IntegerField( default=1) #Int field
    price=models.IntegerField( default=2)
    image=models.ImageField(upload_to="main_app/static/uploads", default="")
    toys = models.ManyToManyField(Toy)
    def __str__(self):
        return f"{self.animal}"
    
    
    def fed_for_today(self):
        return self.feeding_set.filter(date= date.today()).count() >= len(MEALS)
     
    def get_absolute_url(self):
        return reverse('detail',kwargs={'animal_id':self.id})
    
    
    
    
class Feeding(models.Model):
    date = models.DateField('Feeding Date')
    meal = models.CharField(max_length=1,
                            choices=MEALS , default=MEALS[0][0])
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE )
    
    def __str__(self):
        return f"{self.animal.animal} {self.get_meal_display()} on {self.date} "
    
    class Meta:
        ordering = ['-date'] #Date ascending
    
