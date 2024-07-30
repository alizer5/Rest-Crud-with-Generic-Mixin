
from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stu/', views.StudentListCreate.as_view()),
    path('stu/<int:pk>/', views.StudentUpDel.as_view()),

]
