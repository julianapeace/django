from django.db import models
from django.conf import settings #

# Create your models here.

class Publication(models.Model):
  name = models.CharField(max_length=280) # just like peewee
  slug = models.SlugField(max_length=50, unique=True) #want each slug to be unique

  def __str__(self):
      return self.name #problem: in admin page, the publication shows up as publication object because it doesnt recognize it as a string. this method says when you try to convert this obj to string, use the name.
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Post(models.Model):
  title = models.CharField(max_length=50)
  image = models.FileField(null=True, blank=True)
  subtitle = models.CharField(max_length=140,
                              blank=True, null=True)
  slug = models.SlugField(max_length=50, unique=True)
  body = models.TextField()
  created = models.DateTimeField(auto_now=False, auto_now_add=True)
  updated = models.DateTimeField(auto_now=True, auto_now_add=False)
  blog = models.ForeignKey(Publication) #have a fk that points to publications
  categories = models.ForeignKey(Category)
  author = models.ForeignKey(settings.AUTH_USER_MODEL) #must import settings first. line 2. point to tht e authorized users model.
  def __str__(self):
      return self.title
  class Meta:
      ordering = ['-created', '-updated'] # you most likely want to see post ordered backwards. so you want to add the "-"
      # everytime you look at posts, it will always show in this order
class Comment(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post)
    karma = models.BooleanField()
