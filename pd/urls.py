from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('getData',views.getData, name='getData'),
    path('getDataTremor',views.getDataTremor, name='getDataTremor'),
    path('getDataBrady',views.getDataBrady, name='getDataBrady'),   
    path('getDataGait',views.getDataGait, name='getDataGait')
]