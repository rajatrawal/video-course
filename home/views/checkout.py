from django.shortcuts import render,redirect
from django.http import HttpResponse
from home.models import Course,Payment,UserCourse, CouponCode
import razorpay
from coursey.settings import KEY_ID,KEY_SECRET
from time import time
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import json

@login_required
def checkout(request,slug):
    user = request.user
    course = Course.objects.get(slug=slug)
    order=None
    payment = None
    coupon_code = request.GET.get('coupon_code')
    is_exist=UserCourse.objects.filter(course=course,user=user).exists()


    amount,discount,is_valid = get_amount(coupon_code,course)
    # if not is_valid and coupon_code is not None:
    #         return JsonResponse(json.dumps({'status':'error','data':'Please Enter Valid Code'}),safe=False)
    
    
    # if  request.GET.get('action') != 'create_payment' and  is_valid:    
    #     return JsonResponse(json.dumps({'status':'valid','data':' Valid Code','discount':discount,'amount':amount}),safe=False)

    if (request.GET.get('action')=='create_payment' and not is_exist ):        
        if amount <= 0:
            user_course = UserCourse.objects.create(course=course,user= user)
            user_course.save()
            return render(request,'home/my_courses.html',get_my_courses(request.user))
        
        client = razorpay.Client(auth=(KEY_ID, KEY_SECRET))
        currency = 'INR'
        note = {
            'email':user.email,
        }
        receipt = f'coursey-{int(time())}'
        data = {
            'amount':amount*100,
            'currency':currency,
            'receipt':receipt,
            'notes':note
        }
        order = client.order.create(data=data)
        payment = Payment.objects.create(order_id=order.get('id'),user=user,course=course)
        payment.save()
    elif not is_valid and coupon_code is not None:
            return JsonResponse(json.dumps({'status':'error','data':'Please Enter Valid Code'}),safe=False)
        
    elif request.GET.get('action') != 'create_payment' and  is_valid:    
        return JsonResponse(json.dumps({'status':'valid','data':' Valid Code','discount':discount,'amount':amount}),safe=False)
    
    
    params={'course':course,'order':order,'payment':payment,'is_exist':is_exist}
    return render(request,'home/checkout.html',params) 

def get_amount(coupon_code,course):
    mrp = course.price
    discount = course.discount
    amount = int(mrp-(mrp*discount*0.01))
    try:
        coupon_obj = CouponCode.objects.get(code=coupon_code,course=course)

        discount = coupon_obj.discount
        return int(amount-(amount*discount*0.01)),discount,True
    except Exception:
        return amount,discount,False
    
    
    
def get_my_courses(user):
    user_courses = UserCourse.objects.filter(user=user)
    courses = [i.course for i in user_courses]
    return {'courses':courses}
    
@csrf_exempt
def verify_payment(request):
    if request.method == 'POST':
        razorpay_payment_id= request.POST.get('razorpay_payment_id')
        razorpay_order_id = request.POST.get('razorpay_order_id')
        razorpay_signature= request.POST.get('razorpay_signature')
        client = razorpay.Client(auth=(KEY_ID, KEY_SECRET))

        response = client.utility.verify_payment_signature(
            {
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': razorpay_payment_id,
                'razorpay_signature': razorpay_signature,
            }
        )
        if response:
            try:
                payment = Payment.objects.get(order_id=razorpay_order_id)
                payment.payment_id = razorpay_payment_id
                user_course = UserCourse.objects.create(course=payment.course,user= payment.user)
                user_course.save()
                payment.user_course = user_course
                payment.status = True
                payment.save()
            except Exception:
                return redirect('home')
         
            
            return render(request,'home/my_courses.html',get_my_courses(request.user))
    return redirect('home')

@login_required
def my_course(request):
    return render(request,'home/my_courses.html',get_my_courses(request.user))
