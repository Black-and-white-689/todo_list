from django.contrib.auth.decorators import login_required

from django.contrib.auth.mixins import LoginRequiredMixin

from django.db.models import Q

from django.shortcuts import render

from django.urls import reverse_lazy

from django.views import generic

from .models import Task, Tag

from django.utils import timezone

from .forms import (
    TaskForm,
    TaskSearchForm,
    TagSearchForm,
)


@login_required
def index(request):
    #  main_page

    #  Full date now
    now = timezone.now()
    current_month = now.month
    current_year = now.year

    #  Done task in this month
    tasks_done_this_month = Task.objects.filter(
        is_done=True,
        deadline__year=current_year,
        deadline__month=current_month,
    )

    #  Full statistics
    num_tasks_total = Task.objects.count()
    num_tasks_done = Task.objects.filter(is_done=True).count()
    num_tasks_pending = Task.objects.filter(is_done=False).count()

    #  Visits
    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_tasks_total": num_tasks_total,
        "num_tasks_done": num_tasks_done,
        "num_tasks_pending": num_tasks_pending,
        "tasks_done_this_month": tasks_done_this_month,
        "current_month": now.strftime("%B"),
        "num_visits": num_visits + 1,
    }

    return render(request, "todo/index.html", context)


#  Tasks
class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Task
    template_name = "todo/task_list.html"
    context_object_name = "task_list"
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_form"] = TaskSearchForm(self.request.GET)
        return context

    def get_queryset(self):
        queryset = super().get_queryset().select_related(
            "tags")
        query = self.request.GET.get("q")
        if query:
            queryset = queryset.filter(
                Q(name__icontains=query) |
                Q(description__icontains=query)
            )
        return queryset.order_by("id")


class TaskDetailView(LoginRequiredMixin, generic.DetailView):
    model = Task
    template_name = "todo/task_detail.html"


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo:task-list")


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo:task-list")


class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo:task-list")


#  Task_types
class TagListView(LoginRequiredMixin, generic.ListView):
    model = Tag
    template_name = "todo/tag_list.html"
    context_object_name = "tag_list"
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_form"] = TagSearchForm(self.request.GET)
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get("q")
        if query:
            queryset = queryset.filter(name__icontains=query)
        return queryset.order_by("id")


class TagCreateView(LoginRequiredMixin, generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:tag-list")


class TagUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:tag-list")


class TagDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todo:tag-list")
