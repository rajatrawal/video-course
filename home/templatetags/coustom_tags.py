from django import  template
from home.models import UserCourse
register = template.Library()

@register.simple_tag
def cal_saleprice(mrp,discount):
    return round(mrp-(mrp*discount*0.01) if discount != None else mrp)

@register.simple_tag
def is_included(course,user):
    if user.is_authenticated:
        return UserCourse.objects.filter(course=course,user=user).exists()
    return False


@register.filter
def rupee(price):
    return f'₹{price}'


