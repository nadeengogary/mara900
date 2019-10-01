from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
# Dont Repeat Yourself = DRY

# from .forms import ContactForm
# from blog.models import BlogPost

def home_page(request):
	return render(request, "hello_world.html")