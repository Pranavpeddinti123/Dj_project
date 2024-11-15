from django.contrib import auth, messages
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.shortcuts import render

from adminapp.models import StudentList
from facultyapp.models import Marks


# Create your views here.

def studenthomepage(request):
    return render(request, 'facultyapp/StudentHomePage.html')


def UserLoginPageCall(request):
    return render(request, 'adminapp/Login.html')

def UserLoginLogic(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            if len(username) == 10:
                # Redirect to StudentHomePage
                messages.success(request, 'Login successful as student!')
                return redirect('studentapp:StudentHomePage')  # Replace with your student homepage URL name
                return render(request, 'facultyapp/FacultyHomePage.html')
            elif len(username) == 4:
                # Redirect to FacultyHomePage
                messages.success(request, 'Login successful as faculty!')
                return redirect('facultyapp:FacultyHomePage')  # Replace with your faculty homepage URL name
                return render(request, 'facultyapp/FacultyHomePage.html')
            else:
                # Invalid username length
                messages.error(request, 'Username length does not match student or faculty criteria.')
                return render(request, 'adminapp/Login.html')
        else:
            # If authentication fails
            messages.error(request, 'Invalid username or password.')
            return render(request, 'adminapp/Login.html')
    else:
        return render(request, 'adminapp/Login.html')

def logout(request):
    auth.logout(request)
    return redirect('projecthomepage')

def student_list(request):
    students = StudentList.objects.all()
    return render(request, 'adminapp/student_list.html', {'students': students})

def view_marks(request):
    user=request.user
    try:
        student_user = User.objects.get(username=user.username)
        student = StudentList.objects.get(Register_Number=student_user)
        marks = Marks.objects.filter(student=student)
        return render(request,'studentapp/view_marks.html', {'marks':marks})
    except (StudentList.DoesNotExist, User.DoesNotExist):
        return render(request, 'studentapp/view_marks.html',{
            'error': 'No Student record found for this user.'
        })

