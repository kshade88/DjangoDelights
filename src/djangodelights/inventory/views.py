from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse_lazy

from .models import Ingredient, MenuItem, RecipeRequirement, Purchase
from .forms import IngredientForm, MenuItemForm, RecipeRequirementForm, PurchaseForm
  

# Create your views here.
def home(request):
    return render(request, 'inventory/home.html')

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')

def dashboard(request):
    return render(request, 'inventory/dashboard.html')

class IngredientListView(ListView):
    model = Ingredient
    template_name = 'inventory/ingredient_list.html'
    context_object_name = 'ingredients'

class MenuItemListView(ListView):
    model = MenuItem
    template_name = 'inventory/menu_item_list.html'
    context_object_name = 'menu_items'

class RecipeRequirementListView(ListView):
    model = RecipeRequirement
    template_name = 'inventory/recipe_requirement_list.html'
    context_object_name = 'reciperequirements'

class PurchaseListView(ListView):
    model = Purchase
    template_name = 'inventory/purchase_list.html'
    context_object_name = 'purchases'

class IngredientCreateView(CreateView):
    model = Ingredient
    form_class = IngredientForm
    template_name = 'inventory/ingredient_form.html'
    success_url = reverse_lazy('ingredient_list')

class MenuItemCreateView(CreateView):
    model = MenuItem
    form_class = MenuItemForm
    template_name = 'inventory/menu_item_form.html'
    success_url = reverse_lazy('dashboard')

class RecipeRequirementCreateView(CreateView):
    model = RecipeRequirement
    form_class = RecipeRequirementForm
    template_name = 'inventory/recipe_requirement_form.html'
    success_url = reverse_lazy('dashboard')

class PurchaseCreateView(CreateView):
    model = Purchase
    form_class = PurchaseForm
    template_name = 'inventory/purchase_form.html'
    success_url = reverse_lazy('dashboard')

class IngredientUpdateView(UpdateView):
    model = Ingredient
    form_class = IngredientForm
    template_name = 'inventory/ingredient_form.html'
    success_url = reverse_lazy('dashboard')

class MenuItemUpdateView(UpdateView):
    model = MenuItem
    form_class = MenuItemForm
    template_name = 'inventory/menuitem_form.html'
    success_url = reverse_lazy('dashboard')

class RecipeRequirementUpdateView(UpdateView):
    model = RecipeRequirement
    form_class = RecipeRequirementForm
    template_name = 'inventory/reciperequirement_form.html'
    success_url = reverse_lazy('dashboard')

class PurchaseUpdateView(UpdateView):
    model = Purchase
    form_class = PurchaseForm
    template_name = 'inventory/purchase_form.html'
    success_url = reverse_lazy('dashboard')


def logout_view(request):
    logout(request)
    return redirect('login')





