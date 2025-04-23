from django.db import models


class health(models.Model):
    hname = models.CharField(max_length=30)
    hprice = models.IntegerField()
    hinfo = models.TextField()
    hamm = models.CharField(max_length=30,null=True)
    himg= models.ImageField(upload_to='static/imagesv/')
    # himg= models.ImageField(upload_to='imagesv/')


class medicines(models.Model):
    mname = models.CharField(max_length=30)
    mprice = models.IntegerField()
    minfo = models.TextField()
    mamm = models.CharField(max_length=30,null=True)
    mimg= models.ImageField(upload_to='static/imagesg/')
    # mimg= models.ImageField(upload_to='imagesg/')
# Create your models here.


