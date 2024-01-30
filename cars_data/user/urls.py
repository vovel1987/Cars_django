from django.urls import path,include

from .views import *

urlpatterns = [
    path('autos/',  AutosList.as_view()),
    path('models/',ModelsList.as_view()),
    path('autos/<slug:model_id>/',ModelAutos.as_view()),
    path('autos/vehicle/<slug:model_vin>/',ModelAuto.as_view()),
    path('autos/images/',ImagesList.as_view()),
]
