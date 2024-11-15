from django import forms
from .models import Post, AddCourse , Marks


class PostForm(forms.ModelForm):
    class Meta:
        model = Post  # Assuming your model is called Post
        fields = ['title', 'content']  # Include the fields you want to appear in the form
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the title'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your post content here...'}),
        }

class AddCourseForm(forms.ModelForm):
    class Meta:
        model = AddCourse
        fields = ['student', 'course', 'section']

class MarksForm(forms.ModelForm):
    class Meta:
        model = Marks
        fields = ['student' , 'course' , 'marks']