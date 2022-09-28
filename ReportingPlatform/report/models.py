from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class subCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE,)
    subName = models.CharField(max_length=100)
    def __str__(self):
        return self.subName  

class Report(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    category = models.IntegerField()
    sub_category = models.IntegerField()
    subject = models.CharField(max_length=200)
    