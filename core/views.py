from django.shortcuts import render
from django.views.generic import TemplateView


def home(request):
    return render(request, 'test/index.html')



class TestView(TemplateView):
    template_name = "test.html"

