from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.db.models import Count, Prefetch
from django.views import View
# from main.models import Article, LikeArticleUser, Comment, LikeCommentUser

# class Page(View):
#     def get(self, request):
#         context = {}
#         comment_query = Comment.objects.annotate(count_like=Count('users_like'))


def index(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'main/index.html', {'title': 'Главная', 'tasks': tasks})





def about(request):
    return render(request, 'main/about.html')



def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Статья написана некорректно'


    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)