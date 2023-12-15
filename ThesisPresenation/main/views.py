from django.apps import apps
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def models(request):
    app_models = apps.get_app_config("main").get_models()
    data = [{"name": model.__name__, "description": model.__doc__} for model in app_models]
    return render(request, 'models.html', {'all_models': data})


def predefined_functions(request):
    return render(request, 'functions.html')


def model(request, model_name):
    return render(request, 'model.html', {'name': model_name})
