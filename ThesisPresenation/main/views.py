from django.apps import apps
from django.shortcuts import render
from ThesisPresenation.main.logic.predefined_functions import PredefinedFunctions


def index(request):
    return render(request, 'index.html')


def models(request):
    app_models = apps.get_app_config("main").get_models()
    data = [{"name": model.__name__, "description": model.__doc__} for model in app_models]
    return render(request, 'models.html', {'all_models': data})


def predefined_functions(request):
    my_instance = PredefinedFunctions()
    all_functions = [
        method for method in dir(my_instance) if callable(getattr(my_instance, method)) and not method.startswith("__")
    ]
    return render(request, 'functions.html', {'all_functions': all_functions})


def model(request, model_name):
    model_of_name = apps.get_model(app_label='main', model_name=model_name)
    data = [
        {"field_name": field.name, "field_type": type(field).__name__}
        for field in model_of_name._meta.fields
    ]
    return render(request, 'model.html', {'model_name': model_name, "data": data})
