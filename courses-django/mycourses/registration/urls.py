from . import views
from django.urls import path

urlpatterns = [
    path('', views.firstapi),
    path('<int:id>/', views.fetchDetails),
    path('students/', views.StudentView.as_view()),
]