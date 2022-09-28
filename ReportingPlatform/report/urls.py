from django.urls import path
from . import views


urlpatterns = [
    path('', views.report, name='report'),
    path('add/', views.add, name='add'),
    path('add/ajax/load-subCats/', views.loadSubCats, name='ajax_load_subCats'),
    path('showAll/', views.showAll, name='show-all'),
    path('deleteAll/', views.deleteAll, name='delete-all'),
    path('delete/', views.delete, name='delete'),
    path('message/', views.message, name='message'),  
] 