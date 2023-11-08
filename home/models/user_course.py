from django.db import models
from . course import Course
from django.contrib.auth.models import User
class UserCourse(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE,related_name='userCourse')
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='userCourse')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.course}-{self.user}"