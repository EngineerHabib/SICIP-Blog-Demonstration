from django.urls import path
from blogs.views import*

urlpatterns = [
    path('',Login_page,name='Login_page'),
    path('home/',Home,name='Home'),
    path('register/',Register_page,name='Register_page'),
    path('blog/',Blog_list,name='Blog_list'),
    path('Add_Blog/',Add_Blog,name='Add_Blog'),
    path('Blog_view/',Blog_view,name='Blog_view'),
    path('Update_Blog/<str:id>/',Update_Blog,name='Update_Blog'),
    path('Delete_blog/<str:id>/',Delete_blog,name='Delete_blog'),


    path('logout/',Logout_page,name='Logout_page'),
]