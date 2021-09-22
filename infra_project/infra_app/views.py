from django.http import HttpResponse


def index(request):
    return HttpResponse('With hope in your heart And youll never walk alone!')


def second_page(request):
    return HttpResponse('А это вторая страница!')
