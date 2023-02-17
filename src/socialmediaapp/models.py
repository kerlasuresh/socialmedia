from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.utils.text import slugify


class Articale_list(models.Model):
    title=models.CharField(max_length=100)
    slug=models.CharField(max_length=100,blank=True,null=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    likes=models.ManyToManyField(User,related_name='likes')
    created_date=models.DateField(max_length=50)
    body=models.CharField(max_length=500)

    def get_absolute_url(self):
        return reverse('articledetaile',args=[self.id,self.slug])
    def total_likes(self):
        return self.likes.count()


@receiver(pre_save,sender=Articale_list)
def pre_save_slug(sender,**kwargs):
    slug1 = slugify(kwargs['instance'].title)
    kwargs['instance'].slug=slug1
