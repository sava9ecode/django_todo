from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect

from .forms import TaskForm
from .models import Task
from category.models import Category


@login_required
def frontpage(request):
    if request.method == "POST":
        form = TaskForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            form.save()

            messages.success(request, "The task was added", extra_tags="is-success")
    else:
        form = TaskForm()

    title = "This is a variable"
    tasks = Task.objects.filter(user=request.user)
    categories = Category.objects.all()

    page = request.GET.get("page", 1)
    paginator = Paginator(tasks, 10)
    try:
        tasks = paginator.page(page)
    except PageNotAnInteger:
        tasks = paginator.page(1)
    except EmptyPage:
        tasks = paginator.page(tasks.num_pages)

    return render(
        request,
        "task/frontpage.html",
        {"title": title, "tasks": tasks, "categories": categories, "form": form},
    )


@login_required
def edit_task(request, pk):
    task = Task.objects.filter(user=request.user).get(pk=pk)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            form.save()
            return redirect("frontpage")
    else:
        form = TaskForm(instance=task)

    return render(request, "task/edit_task.html", {"form": form})


@login_required
def mark_completed(request, pk):
    task = Task.objects.filter(user=request.user).get(pk=pk)
    task.is_done = True
    task.save()

    return redirect("frontpage")


@login_required
def delete_task(request, pk):
    task = Task.objects.filter(user=request.user).get(pk=pk)
    task.delete()

    return redirect("frontpage")


@login_required
def search(request):
    query = request.GET.get("query", "")

    if query:
        tasks = Task.objects.filter(user=request.user).filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )
    else:
        tasks = []

    return render(request, "task/search.html", {"query": query, "tasks": tasks})
