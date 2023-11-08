from django.db import models
from .user_course import UserCourse
from . course import Course
from django.contrib.auth.models import User

class Payment(models.Model):
    order_id = models.CharField(max_length=100,null=False,blank=True)
    payment_id = models.CharField(max_length=100,null=True,blank=True)
    user_course = models.ForeignKey(UserCourse,on_delete=models.CASCADE,null=True,related_name='payment',blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,related_name='payment')
    course = models.ForeignKey(Course,on_delete=models.CASCADE,null=True,related_name='payment')
    date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return f"{self.user_course}"
    