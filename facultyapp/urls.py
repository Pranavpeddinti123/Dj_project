from django.urls import path, include
from . import views
app_name = 'facultyapp'
urlpatterns = [
    path('FacultyHomePage/', views.facultyhomepage, name="FacultyHomePage"),
    path('add_post/', views.add_post, name='add_post'),
    path('<int:pk>/delete/', views.delete_post, name='delete_post'),
    path('add_course/', views.add_course, name='add_course'),
    path('add_view_student_list/', views.view_student_list, name='add_view_student_list'),
    path('post_marks/', views.post_marks, name='post_marks'),
]