from django.shortcuts import render, get_object_or_404
from django.db.models import Prefetch, Q
from .models import Pizza, Category


def pizza_list(request):
    template_name = 'pizza/pizza_list.html'
    search_query = request.GET.get('search', '')
    pizza_list = (
        Pizza.objects
        .filter(
            Q(title__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(structure__icontains=search_query) |
            Q(category__title__icontains=search_query),
            is_published=True,
        )
        .distinct()
        .prefetch_related(
            Prefetch(
                'category',
                queryset=Category.objects.filter(
                    is_published=True,
                )
            )
        )
    )
    context = {
        'pizza_list': pizza_list,
    }

    return render(request, template_name, context)


def pizza_detail(request, pk):
    template_name = 'pizza/pizza_detail.html'

    pizza_det = get_object_or_404(
        Pizza.objects
        .filter(
            is_published=True,
        ).prefetch_related(
            Prefetch(
                'category',
                queryset=Category.objects.filter(
                        is_published=True
                    )
            )
        ),
        pk=pk
    )
    context = {
        'pizza': pizza_det,
    }

    return render(request, template_name, context)
