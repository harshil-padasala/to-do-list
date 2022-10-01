from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Task

from django.contrib.auth.views import LoginView

# Create your views here.

class CustomLoginView(LoginView):
    """
    This class is used for login purprse.
    """
    template_name = 'main/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self) -> str:
        return reverse_lazy('task-list')


class TaskList(ListView):
    """
    This class is used for displaying list of Task using ListView.
    """
    model = Task 
    context_object_name = 'tasks'

class TaskDetail(DetailView):
    """
    This class is used for displaying details of particular task using DetailView.
    """
    model = Task
    context_object_name = 'task'
    template_name = 'main/task.html'

class TaskCreate(CreateView):
    """
    This class is used for creating a new task.
    """
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('task-list')

class TaskUpdate(UpdateView):
    """
    This class is used for updating a task.
    """
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('task-list')

class TaskDelete(DeleteView):
    """
    This class is used for deleting a task.
    """
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('task-list')
