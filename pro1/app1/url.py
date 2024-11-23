from django.urls import path
from app1 import views
urlpatterns = [
   
    path('Login',views.Login_page,name='Login'),
    path('Register',views.Register_page,name='Register'),
    path('',views.StudentData,name='')

]
