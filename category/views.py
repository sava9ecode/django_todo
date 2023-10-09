from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Category


@login_required
def category_detail(request, pk):
    category = Category.objects.get(pk=pk)
    categories = Category.objects.all()

    return render(
        request,
        "category/detail.html",
        {"categories": categories, "category": category},
    )
