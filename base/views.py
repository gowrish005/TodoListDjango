from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView , UpdateView,  DeleteView, FormView
from django.urls import reverse_lazy
from django.http import HttpResponse, Http404
import os
from pathlib import Path

from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Task


class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')
    
class RegisterPage(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage,self).form_valid(form)
    



# Create your views here.
def serve_static_file(request, filename):
    # Path to templates/base directory
    base_dir = Path(__file__).resolve().parent
    file_path = os.path.join(base_dir, 'templates', 'base', filename)
    
    if os.path.exists(file_path):
        with open(file_path, 'rb') as f:
            file_content = f.read()
        
        # Set content type based on file extension
        content_type = 'text/plain'
        if filename.endswith('.js'):
            content_type = 'application/javascript'
        elif filename.endswith('.css'):
            content_type = 'text/css'
        
        return HttpResponse(file_content, content_type=content_type)
    else:
        raise Http404("File not found")

class TaskList(LoginRequiredMixin,ListView):
    model = Task
    context_object_name = "tasks"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count() # count of incomplete tasks
        return context

class TaskDetail(LoginRequiredMixin,DetailView):
    model = Task
    context_object_name = "task"
    template_name = 'base/task.html'

class TaskCreate(LoginRequiredMixin,CreateView):
    model = Task
    fields = ['title','description','complete']
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    

class TaskUpdate(LoginRequiredMixin,UpdateView):
    model = Task
    fields = ['title','description','complete']
    success_url = reverse_lazy('tasks')

class DeleteView(LoginRequiredMixin,DeleteView):
    model = Task
    context_object_name  = 'task'
    success_url = reverse_lazy('tasks')

