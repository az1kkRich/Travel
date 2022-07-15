from django.db import models

# Create your models here.

class MazzaQilingYayrang(models.Model):
    name = models.CharField(max_length=50)
    malumoti = models.TextField()
    narxi = models.IntegerField()
    taklif = models.BooleanField()
    image = models.ImageField(upload_to='MazzaQilibYayra')
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        verbose_name = ("Malumot")
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class News(models.Model):
    name = models.CharField(max_length=50)
    malumoti = models.TextField()
    narxi = models.IntegerField()
    taklif = models.BooleanField()
    image = models.ImageField(upload_to='news')
    slug = models.SlugField(max_length=100, unique=True)
    date = models.DateTimeField(auto_created=True)

    class Meta:
        verbose_name = ("Yangiliklar")
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name