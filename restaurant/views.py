# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import UpdateView
from django.shortcuts import render,get_object_or_404
from .models import *

from django.http import HttpResponse

# Create your views here.

def HomePage(request):
    top_restaurants=restaurant.objects.order_by('rate').reverse()[:10]
    return render(request,'HomePage.html',{'restaurants':top_restaurants})


def restaurant_page(request,pk,name):
    rest=restaurant.objects.filter(pk=pk).get()
    me=menu.objects.filter(restaurant=rest).get()
    foods=food.objects.filter(menu=me)
    # ingre={}
    # for f in foods:
    #     ingre[f.pk]=ingredients.objects.filter(food=f)
    return render(request,'restaurant_page.html',{'restaurant':rest,'foods':foods})
                                                  # 'ingredients':ingre})

def ingredients_call(request,foo):
    print("hey")
    ingre=ingredients.objects.filter(food=foo)
    print(ingre)
    return render(request,'restaurant_page.html',{'ingredients':ingre})


# class ItemUpdateView(UpdateView):
#     model = ingredients
#     form_class = ingredients
#     template_name = 'templates/ingredients_show.html'
#
#     def dispatch(self, *args, **kwargs):
#         self.ingredients = kwargs['pk']
#         return super(ItemUpdateView, self).dispatch(*args, **kwargs)
#
#     def form_valid(self, form):
#         form.save()
#         item = Item.objects.get(id=self.item_id)
#         return HttpResponse()