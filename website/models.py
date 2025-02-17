from datetime import datetime
from django.db import models
from django_countries.fields import CountryField




  
class branches(models.Model):   
  branch_name  = models.CharField(max_length=100,null=True, default='')
  branch_address  = models.CharField(max_length=100,null=True)
  branch_url  = models.URLField(max_length = 300,null=True) 
  branch_image = models.ImageField(null=True, blank=True, upload_to="branches/")
  def __str__(self):
    return self.branch_name
  
class gallery(models.Model):   
  event_name  = models.CharField(max_length=100,null=True, default='')
  event_image = models.ImageField(null=True, blank=True, upload_to="Gallery/")
  def __str__(self):
    return self.event_name
  
class BlogDetails(models.Model):   
  blog_event_name  = models.CharField(max_length=100, default='')
  blog_description  = models.CharField(max_length=1000,null=True, default='')
  blog_event_image = models.ImageField(null=True, blank=True, upload_to="Blogs/")
  posted_date = models.DateTimeField(default=datetime.now)

  def __str__(self):
    return self.blog_event_name
  
class Promo(models.Model):   
  promo_name  = models.CharField(max_length=100,null=True, default='')
  promo_image = models.ImageField(null=True, blank=True, upload_to="promotion/")
  start_date = models.DateField()
  end_date = models.DateField()
  def __str__(self):
    return self.promo_name
  
class careermodel(models.Model):
  FEMALE = 'FEMALE'
  MALE = 'MALE'
  NONE = 'NONE'
  APPROVED = "APPROVED"
  REJECTED = "REJECTED" 
  PENDING ="PENDING"

  GENDER = [
        (FEMALE, "Female"),
        (MALE, "Male"),
        (NONE, "Prefer not to say"),
    ]
  status_select = [
        (APPROVED, "approved"),
        (REJECTED, "rejected"),
        (PENDING, "pending"),
        
    ]



  first_name = models.CharField(max_length=75)
  Last_name = models.CharField(max_length=75)
  gender = models.CharField(max_length=20,choices=GENDER,default=NONE,)
  phone_no = models.CharField(max_length=30)
  email = models.EmailField(max_length=150)
  nationality = CountryField(blank_label="(select country)")
  current_location = CountryField(blank_label="(select country)")
  age = models.IntegerField(default='')
  attach_cv = models.FileField(upload_to='attachment_cv/')
  status = models.CharField(
        max_length=20,
        choices=status_select,
        default=PENDING,
    )
  
  def __str__(self):
    return self.first_name




  
  
  