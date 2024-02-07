from django.urls import path,include

from .views import *

urlpatterns = [
    
    path('models/',ModelsList.as_view()),
    
    path('media/images/<slug:model>/',ImageList.as_view()),
    path('bewertungs/',BewertungList.as_view()),
    path('bewertungs/<slug:auto>/',BewertungAuto.as_view()),
    path('status/auto/<slug:auto>/',AutoZubehorList.as_view()),
    path('status/reifen/<slug:auto>/',AutoReifenList.as_view()),
    path('status/lack/<slug:auto>/',AutoLackMessungList.as_view()),

    path('autos/update/',AutoUpdateView.as_view()),
    path('autos/post/',AutoPostView.as_view()),
    path('autos/vehicle/<slug:model_id>/',ModelAuto.as_view()),
    path('autos/',  AutosList.as_view()),
    path('autos/<slug:model_id>/',ModelAutos.as_view()),

]
