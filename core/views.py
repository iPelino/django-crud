from django.shortcuts import render
from django.views.generic import TemplateView,CreateView, ListView,DetailView
from core.models import Student
from django.contrib.auth.models import PermissionsMixin

def home(request):
    return render(request, 'test/index.html')



class TestView(TemplateView):
    template_name = "test.html"



class StudentCreateView(CreateView):
    model = Student
    fields = ['reg_number', 'first_name', 'last_name', 'age', 'email']
    success = 'home'
    template_name = "register.html"



class StudentListView(ListView):
    model = Student
    template_name = "list_students.html"


class StudentDetailView(DetailView):
    model = Student
    template_name = "student_detail.html"




