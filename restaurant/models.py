# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class restaurant(models.Model):
    name = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='pictures', null=True, blank=True)
    city = models.CharField(max_length=500, null=True)
    address = models.TextField(null=True)
    tell = models.CharField(max_length=8, null=True)
    date_joined = models.DateField(auto_now_add=True)
    viwed_num = models.IntegerField(default=0)
    rate = models.FloatField(default=0.0)

    def __str__(self):
        return self.name


class menu(models.Model):
    restaurant = models.ForeignKey(restaurant, on_delete=models.CASCADE)


class food(models.Model):
    name = models.CharField(max_length=200,null=True)
    image = models.ImageField(upload_to='pictures',null=True, blank=True)
    description = models.TextField(null=True)
    price = models.FloatField(default=0)
    ordered_num = models.IntegerField(default=0)
    rate = models.FloatField(default=0.0)
    menu = models.ForeignKey(menu, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.name


class ingredients(models.Model):
    name = models.CharField(max_length=200,null=True)
    image = models.ImageField(upload_to='pictures',null=True, blank=True)
    description = models.TextField(null=True)
    price = models.FloatField(default=0)
    ordered_num = models.IntegerField(default=0)
    rate = models.FloatField(default=0.0)
    food = models.ForeignKey(food, on_delete=models.CASCADE,null=True)
