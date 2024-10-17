from django.shortcuts import render
from django.db.models import Prefetch
from pizza.models import Pizza, Category


def home(request):
    template_name = 'homepage/home.html'

    pizza_list = (
        Pizza.objects
        .filter(
            is_on_main=True,
            is_published=True,
        )
        .order_by(
            'output_order',
            'title',
        )
        .prefetch_related(
            Prefetch(
                'category',
                queryset=Category.objects.filter(
                        is_published=True
                    ).order_by(
                        'output_order',
                        'title',
                    )
            )
        )
    )
    context = {
        'pizza_list': pizza_list,
    }
    return render(request, template_name, context)
