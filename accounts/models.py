
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

# class User(AbstractUser):
#   USER_TYPE_CHOICES = (
#       (1, 'restaurant'),
#       (2, 'customer'),
#   )
#
#   user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)



class customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    email=models.EmailField()
    image = models.ImageField(upload_to='pictures', null=True, blank=True)
    city = models.CharField(max_length=500, null=True)
    address = models.TextField(null=True)
    date_joined = models.DateField(auto_now_add=True)

    @receiver(post_save, sender=User)
    def update_user_profile(sender, instance, created, **kwargs):
        if created:
            customer.objects.create(user=instance)
        instance.customer.save()


# class restaurant(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
#     name = models.CharField(max_length=200, null=True)
#     image = models.ImageField(upload_to='pictures', null=True, blank=True)
#     city = models.CharField(max_length=500, null=True)
#     address = models.TextField(null=True)
#     tell = models.CharField(max_length=8, null=True)
#     date_joined = models.DateField(auto_now_add=True)
#     viwed_num = models.IntegerField(default=0)
#     rate = models.FloatField(default=0.0)


