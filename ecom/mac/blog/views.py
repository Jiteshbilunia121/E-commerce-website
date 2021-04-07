from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Blogpost

def index(request):
    mypost=Blogpost.objects.all()
    print(mypost)
    return render(request, 'blog/index.html',{'mypost':mypost})
   
def blogpost(request, id):    
    post = Blogpost.objects.filter(post_id = id)[0]
    print(post)  
    return render(request, 'blog/blogpost.html', {'post':post} ) 

# Create your views here.
      