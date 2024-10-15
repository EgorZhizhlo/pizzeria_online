from django.shortcuts import render


def about_pizzeria(request):
    tempalte_name = 'about/about_pizzeria.html'

    context = {}

    return render(request, tempalte_name, context)
