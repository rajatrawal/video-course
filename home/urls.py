from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

urlpatterns = [
   path('',HomePageView.as_view(),name="home"),
   path('course/<str:slug>',get_course,name="get_course"),
   path('signUp/',sign_up,name="sign_up"),
   path('signIn/',sign_in,name="sign_in"),
   path('signOut/',sign_out,name="sign_out"),
   path('verifyPayment/',verify_payment,name="verify_payment"),
   path('myCourses/',my_course,name="my_courses"),
   path('search/',search,name="search"),
   path('checkout/<str:slug>',checkout,name="checkout"),
   
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



