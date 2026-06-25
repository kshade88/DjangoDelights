from django.db import models

# Create your models here.

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    unit = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} ({self.quantity} {self.unit})"

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    ingredients = models.ManyToManyField(Ingredient)

    def __str__(self):
        return self.name

class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity_required = models.IntegerField()

    def __str__(self):
        return f"{self.quantity_required} {self.ingredient.unit} of {self.ingredient.name} for {self.menu_item.name}"

class Purchases(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    purchase_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.quantity} x {self.menu_item.name} purchased on {self.purchase_date}"