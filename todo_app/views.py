from django.contrib.auth.decorators import login_required

from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import render, redirect

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
    tasks = Task.objects.all().prefetch_related("tags").order_by(
        "is_done",
        "-created_at"
    )

    return render(request, "todo/index.html", {"tasks": tasks})


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
        queryset = Task.objects.all().prefetch_related("tags")
        query = self.request.GET.get("q")
        if query:
            queryset = queryset.filter(content__icontains=query)

        return queryset.order_by("is_done", "-created_at")


class TaskDetailView(LoginRequiredMixin, generic.DetailView):
    model = Task
    template_name = "todo/task_detail.html"


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    form_class = TaskForm
    template_name = "todo/task_detail.html"
    success_url = reverse_lazy("todo:task-list")


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "todo/task_detail.html"
    success_url = reverse_lazy("todo:task-list")


class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task
    template_name = "todo/task_detail.html"
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
    template_name = "todo/tag_form.html"
    success_url = reverse_lazy("todo:tag-list")


class TagUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Tag
    fields = "__all__"
    template_name = "todo/tag_form.html"
    success_url = reverse_lazy("todo:tag-list")


class TagDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Tag
    template_name = "todo/tag_form.html"
    success_url = reverse_lazy("todo:tag-list")


@login_required
def toggle_status(request, pk):
    task = Task.objects.get(pk=pk)
    task.is_done = not task.is_done
    task.save()
    return redirect("todo:task-list")
