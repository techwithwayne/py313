from django.shortcuts import render

# Create your views here.

posts = [
    {
        'author': 'Wayne Hatter',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'February 19, 2025'
    },
    {
        'author': 'Enyaw Rettah',
        'title': 'Blog Post21',
        'content': 'Second post content',
        'date_posted': 'February 20, 2025'
    }
]
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')