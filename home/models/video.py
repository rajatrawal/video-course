from django.db import models
from .course import Course

class Video(models.Model):
    title = models.CharField(null=False,blank=False,max_length=100)
    course = models.ForeignKey(Course,on_delete=models.CASCADE,blank=False,null=False,related_name="videos")
    serial_number = models.IntegerField(default=0,null=False,blank=False)
    video_id=models.CharField(max_length=100,null=False,blank=False)
    is_preview = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title