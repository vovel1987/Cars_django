from django.urls import path,include

from .views import *

urlpatterns = [
    path('autos/',  AutosList.as_view()),
    path('models/',ModelsList.as_view()),
]
