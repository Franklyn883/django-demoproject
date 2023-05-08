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
    price = models.IntegerField()
    category_id= models.ForeignKey(MenuCategories, on_delete=models.PROTECT, default=None, related_name="category_name")
#The category is the FK that connects the Menu table to the MenuCategories. This is a one to many relationship, since
#many Menu can only belong to one MenuCategories. The on_delete = models.PROTECT
    def __str__(self):
        return self.name + ":" + self.cuisine + "->" + str(self.price)
    

