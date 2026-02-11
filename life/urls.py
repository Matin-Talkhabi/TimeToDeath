from django.urls import path
from . import views

app_name = 'life'

urlpatterns = [
    path('', views.index, name='index'),
    path('results/<str:unique_id>/', views.results, name='results'),
    path('pdf/<str:unique_id>/', views.generate_pdf, name='generate_pdf'),
]
