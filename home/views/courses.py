from django.shortcuts import render,redirect
from home.models import Course,Video,UserCourse



def get_course(request,slug):  # sourcery skip: avoid-builtin-shadow
    user_is_auth = request.user.is_authenticated
    # try:
    course = Course.objects.get(slug=slug)
    is_purchased=get_is_purchased(course,request)
    try:
        id = request.GET.get('code')
        video = Video.objects.get(video_id=id)
    except Exception:
        video = Video.objects.filter(course=course).order_by('serial_number').first()

    video_number = video.serial_number
    id = video.video_id
    print(id)
    next_video_id = return_video_id(Video.objects.filter(serial_number= video_number + 1,course=course))
    prev_video_id = return_video_id(Video.objects.filter(serial_number= video_number - 1,course=course))
    
    if video.is_preview is False:

        if (user_is_auth is False):
            return redirect('sign_in')
        else:
            if not is_purchased:
                return redirect('checkout',slug=slug)

    # except Exception:
    #     params={'course':'none'}
    #     return render(request,'home/course.html',params)

    params={'course':course,'id':id,'is_purchased':is_purchased,'next_video_id':next_video_id,'prev_video_id':prev_video_id}
    print(params)
    return render(request,'home/course.html',params)

def return_video_id(video):
    return video.first().video_id if len(video) != 0 else False
        

def get_is_purchased(course,request):
    try:
        is_purchased=   UserCourse.objects.get(course=course,user=request.user)
    except Exception:
        return False
    return True

    
    
    
    
    