from django.db import models

class Food(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
            return self.name

class Choice(models.Model):
    foodnum = models.ForeignKey(Food, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
