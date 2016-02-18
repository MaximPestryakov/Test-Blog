from django.http import HttpResponse
from django.shortcuts import render
from .models import Post
from django.contrib.auth import authenticate, logout, login
from django.http import JsonResponse

def posts(request):
  posts_list = Post.objects.order_by('-created_date')
  return render(request, 'posts.html', {'title': 'Test Blog', 'posts': posts_list})

def get_post(request):
  if request.method == 'POST':
    id = request.POST.get('id', '')
    post = Post.objects.filter(pk=id).values('title', 'text')[0]
    return JsonResponse(post)

def new_post(request):
  if request.method == 'POST':
    title = request.POST.get('title', '')
    text = request.POST.get('text', '')
    Post.objects.create(author=request.user, title=title, text=text)
    return HttpResponse('{}')
  
def user_login(request):
  if request.method == 'POST':
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = authenticate(username=username, password=password)
    if user is not None:
      if user.is_active:
        login(request, user)
        return JsonResponse({'id': user.pk, 'error': 'ok'})
      else:
        return JsonResponse({'error': 'disabled'})
    else:
      return JsonResponse({'error': 'incorrect'})
    
def user_logout(request):
  logout(request)
  return HttpResponse('{}')
