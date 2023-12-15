from django.urls import path
from .views import index, models, predefined_functions, model

urlpatterns = [
    path('', index, name='index'),
    path('models', models, name='models'),
    path('functions', predefined_functions, name='functions'),
    path('models/<str:model_name>/', model, name='model'),
]
