from django.db import models
from django.conf import settings #

# Create your models here.
class Class_Material(models.Model):
    upload = models.FileField(upload_to='uploads/%Y/%m/%d/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class Level(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Volunteer(models.Model):
    sector_name = models.CharField(max_length=50)

    def __str__(self):
        return self.sector_name

class Class(models.Model):
    name = models.CharField(max_length=50)
    level = models.ForeignKey(Level)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    class_level = models.ForeignKey(Class)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    volunteer = models.ForeignKey(Volunteer, null=True)

    def __str__(self):
        return self.name
