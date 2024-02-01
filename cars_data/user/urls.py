from django.urls import path,include

from .views import *

urlpatterns = [
    path('autos/',  AutosList.as_view()),
    path('models/',ModelsList.as_view()),
    path('autos/<slug:model_id>/',ModelAutos.as_view()),
    path('autos/vehicle/<slug:model_id>/',ModelAuto.as_view()),
    path('media/images/<slug:model>/',ImageList.as_view()),
    path('bewertungs/',BewertungList.as_view()),
    path('bewertungs/<slug:auto>/',BewertungAuto.as_view())
]
