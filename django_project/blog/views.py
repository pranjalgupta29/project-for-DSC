from django.shortcuts import render

# Create your views here.

posts = [
    {
        'author' : 'Pranjal Gupta',
        'title' : 'Blog Post 1',
        'content' : 'First Post Content',
        'date_posted' : 'April 9,2020'
    },
    {
        'author' : 'Akshit',
        'title' : 'Blog Post 2',
        'content' : 'Secont Post Content',
        'date_posted' : 'August 10,2020'
    }
]

def home(request):
    context = {
        'posts':posts
    }
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html',{'title' : 'About'})