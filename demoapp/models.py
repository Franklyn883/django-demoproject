from django.db import models

# Create your models here.

#Models in django interacts with the DB to perform CRUD operation
class MenuCategories(models.Model):
    menu_category_name = models.CharField(max_length=200,  default='default_category')

    def __str__(self):
        return self.menu_category_name

class Menu(models.Model):
    name = models.CharField(max_length=100)
    cuisine= models.CharField(max_length=100)
    price = models.IntegerField(null=False)
    category_id= models.ForeignKey(MenuCategories, on_delete=models.PROTECT, default=None, related_name="category_name")
#The category is the FK that connects the Menu table to the MenuCategories. This is a one to many relationship, since
#many Menu can only belong to one MenuCategories. The on_delete = models.PROTECT
    def __str__(self):
        return self.name + ":" + self.cuisine + "->" + str(self.price)
    
#modelform 
#We will create a model our form will inherit from
class Logger(models.Model):
    first_name = models.CharField(max_length=200,)
    last_name = models.CharField(max_length=100)
    time_log = models.TimeField()

#We are making a model, to learn how to use the django admin feature
class Reservation(models.Model):
    name = models.CharField(max_length=200)
    contact = models.CharField('Phone Number', max_length=200)
    time = models.TimeField()
    count = models.IntegerField()
    notes = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name
    


# Giving user permission
# custom permission: This is a Product model with a custom permission "change_category"


