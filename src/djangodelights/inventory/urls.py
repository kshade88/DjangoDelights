from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('ingredients/', views.IngredientListView.as_view(), name='ingredient_list'),
    path('menu_items/', views.MenuItemListView.as_view(), name='menu_item_list'),
    path('recipe_requirements/', views.RecipeRequirementListView.as_view(), name='recipe_requirement_list'),
    path('purchases/', views.PurchaseListView.as_view(), name='purchase_list'),
    path('ingredient/add/', views.IngredientCreateView.as_view(), name='ingredient_add'),
    path('menu_item/add/', views.MenuItemCreateView.as_view(), name='menu_item_add'),
    path('recipe_requirement/add/', views.RecipeRequirementCreateView.as_view(), name='recipe_requirement_add'),
    path('purchase/add/', views.PurchaseCreateView.as_view(), name='purchase_add')
]
