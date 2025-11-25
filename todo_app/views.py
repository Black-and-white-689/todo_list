from django.contrib.auth.decorators import login_required

from django.shortcuts import render

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
