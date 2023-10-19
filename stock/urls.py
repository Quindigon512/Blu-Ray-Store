from django.urls import path
from . import views

app_name = "bluRayInfo"

urlpatterns = [
    path('collection/', views.title, name = "collect"),
    path('add/', views.add, name = "add"),
    path('edit/', views.edit, name = 'edit'),
    path('delete/<int:item_id>/', views.delete, name = 'delete'),
    path('searchMovies/', views.searchMovies, name = 'searchMovies'),
    path('sortMovies/', views.sortMovies, name = 'sortMovies'),
    path('sortID/', views.sortID, name = 'sortID'),
]
