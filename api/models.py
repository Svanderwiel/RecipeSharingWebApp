from django.db import models

# Create your models here.
class Recipe(models.Model):
    food_name = models.CharField(max_length=100, default="", unique=False)
    #publisher
    category = models.CharField(max_length=20, default="Cuisine", unique=False)
    serving_size = models.SmallIntegerField(null=False, default=1)
    last_updated = models.DateTimeField(auto_now_add=True)
    is_public = models.BooleanField(default=False)
    #picture

class User(models.Model):

    first_name = models.CharField(max_length=20, null=False, default="Kona")
    last_name = models.CharField(max_length=30, null=False, default="")



# class Logins(models.Model):
#     login_id
#     user_name
#     password_salt
#     password_hash



