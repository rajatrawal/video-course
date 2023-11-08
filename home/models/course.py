from django.db import models
from django.utils.text import slugify

class Course(models.Model):
    name = models.CharField(max_length=500,blank=False,null=False)
    slug = models.SlugField(default='dfds')
    description = models.TextField(blank=False,null=False)
    price =models.IntegerField(blank=False,null=False,default=0)
    discount = models.IntegerField(default=0,blank=False,null=False)
    active = models.BooleanField(default=False)
    thumbnail = models.ImageField(blank=False,null=False,upload_to="files/thumbnails")
    date = models.DateTimeField(auto_now_add=True)
    resource = models.FileField(blank=False,null=False,upload_to="files/resources")
    length = models.IntegerField(default=0,null=False,blank=False)
    
    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        super(Course,self).save(*args,**kwargs)
    def __str__(self):
        return self.name    

class CourseProperty(models.Model):

    discription = models.CharField(max_length=100 , null=False)
    class Meat:
        abstract =True

class Tag(CourseProperty):
    course = models.ForeignKey(Course,on_delete=models.CASCADE,blank=False,null=False,related_name="tags")
    


    
class Prerequisite(CourseProperty):
   
    course = models.ForeignKey(Course,on_delete=models.CASCADE,related_name="prerequisites",blank=False,null=False)

class Learning(CourseProperty):
    course = models.ForeignKey(Course,on_delete=models.CASCADE,related_name="learnings",blank=False,null=False)
    
class CouponCode(models.Model):
    code = models.CharField(max_length=10)
    course = models.ForeignKey(Course,on_delete=models.CASCADE,related_name="coupon_code")
    discount = models.IntegerField(default=0)
    valid_till = models.DateTimeField()
    