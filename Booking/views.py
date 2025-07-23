from django.shortcuts import render
from .models import *
# Create your views here.
def main_page(request):
    return render(request, 'main/index.html')
