from django.shortcuts import render


def staff_homepage(request):
    return render(request, 'staffUser/index.html', {})
