from django.urls import path
from restaurant import views

urlpatterns = [
    path('', views.HomePage, name='HomePage'),
    path('<pk>/<name>',views.restaurant_page,name='restaurnat_page'),
    # path('<foo>',views.ingredients_call,name='ingredient_show'),
]
