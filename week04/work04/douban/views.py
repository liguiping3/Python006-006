from django.shortcuts import render
from django.http import HttpResponse
from .models import Film_comments

# Create your views here.
def show_comments(request):
  results = Film_comments.objects.filter(stars__gt=3)
  count = results.count()
  return render(request, 'index.html', locals())
