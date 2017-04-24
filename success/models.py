from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
# This model is for general article uploaded by admin or authorized users .
class Articles(models.Model):
    author_admin =models.ForeignKey('auth.User')
    author =models.CharField(max_length=20)
    author_pic = models.FileField(null=True)
    article_title = models.CharField(max_length=500)
    Created_time = models.DateTimeField(default=timezone.now)
    pulished_date = models.DateTimeField(blank=True)
    article_album = models.FileField()
    article_content = models.TextField(null=True)
    article_hit = models.CharField(max_length=300,default="hit")    
    
    def published(self):
        self.pulished_date = timezone.now()
        self.save()
    def __str__(self):
        return self.article_title
   
        # this is the user contact model_form
class Contact(models.Model):
    
        First_name = models.CharField(max_length=250)
        Last_name = models.CharField(max_length=250)
        text_content =models.TextField(null=True)
        email_address= models.EmailField(max_length=250)
        phone_number = models.IntegerField(null=True)
        Country = models.CharField(max_length=2500)
         
        def __str__(self):
            return self.first_name

        def get_absolute_url(self):
                return reverse('success:contacts_list',kwargs={'pk':self.pk})
"""
Random quotes to be displayed in the home page when a user logins in
"""
class Quotes(models.Model):
    quote = models.CharField(max_length=2000,default="Did you also know ,success is not determine by the number of certificates you acquire in life.")
    quote_by = models.CharField(max_length=250,default="ebong")
    def __str__(self):
        return self.quote_by
"""
# User model profile
class Userprofile(models.Model):
    user_name =models.CharField(auth=user)
    gender =models.BooleanField()
    country =models.CharField()
"""
     


    

     
