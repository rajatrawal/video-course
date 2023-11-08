from django.contrib import admin
from . models import *
from django.utils.html import format_html

# Register your models here.

class TagAdmin(admin.TabularInline):
    model =Tag 

class PrerequisiteAdmin(admin.TabularInline):
    model = Prerequisite

class LearningAdmin(admin.TabularInline):
    model = Learning
    
class VideoAdmin(admin.TabularInline):
    model =Video
    
class CourseAdmin(admin.ModelAdmin):
    inlines = [TagAdmin,PrerequisiteAdmin,LearningAdmin,VideoAdmin]
    list_display = ["name",'get_price',"active"]
    list_filter = ["price","active"]
    search_fields = ['course__name']
    def get_price(self,course):
        return f'₹ {course.price}'

class PaymentAdmin(admin.ModelAdmin):
    model=Payment  
    list_display = ['payment_id',"get_user","date","get_course","status"]
    list_filter = ["date","course","status"]
    search_fields = ['course__name','user__email']
    
    def get_user(self,payment):
        return format_html(f"<a target='_blank' href='/admin/auth/user/{payment.user.id}'>{payment.user.email}</a>")
    def get_course(self,payment):
        return format_html(f"<a target='_blank' href='/admin/home/course/{payment.course.id}'>{payment.course.name}</a>")
    
class UserCourseAdmin(admin.ModelAdmin):
    model = UserCourse
    list_display = ['get_course','get_user']
    list_filter =["course","user"]

    def get_user(self,user_course_admin):
        return format_html(f"<a target='_blank' href='/admin/auth/user/{user_course_admin.user.id}'>{user_course_admin.user.email}</a>")
    def get_course(self,user_course_admin):
        return format_html(f"<a target='_blank' href='/admin/home/course/{user_course_admin.course.id}'>{user_course_admin.course.name}</a>")
    
    
class VideoListAdmin(admin.ModelAdmin):
    model = Video
    list_display =["title","serial_number","get_course","is_preview"]
    list_filter = ["is_preview","course"]
    search_fields = ['course__title']
    
    def get_course(self,video):
        return format_html(f"<a target='_blank' href='/admin/home/course/{video.course.id}'>{video.course.name}</a>")
    



admin.site.register(Payment,PaymentAdmin) 
admin.site.register(Course,CourseAdmin) 
admin.site.register(UserCourse,UserCourseAdmin) 
admin.site.register(Video,VideoListAdmin)
admin.site.register(CouponCode)




