from django.shortcuts import render


def my_home(request):
    return render(request, 'recipes/pages/home.html', context={'name': 'Antonio Alan', })
