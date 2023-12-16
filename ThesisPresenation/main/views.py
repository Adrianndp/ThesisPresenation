from django.apps import apps
from django.shortcuts import render
from .logic.helper import get_predefined_functions


def index(request):
    return render(request, 'index.html')


def models(request):
    app_models = apps.get_app_config("main").get_models()
    data = [{"name": model.__name__, "description": model.__doc__} for model in app_models]
    return render(request, 'models.html', {'all_models': data})


def predefined_functions(request):
    all_functions = get_predefined_functions()
    return render(request, 'functions.html', {'all_functions': all_functions})


def model(request, model_name):
    model_of_name = apps.get_model(app_label='main', model_name=model_name)
    data = [
        {"field_name": field.name, "field_type": type(field).__name__}
        for field in model_of_name._meta.fields
    ]
    predefined_f = get_predefined_functions()
    return render(request, 'model.html', {'model_name': model_name, "data": data, "predefined_functions": predefined_f})
