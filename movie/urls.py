from django.urls import path
from . import views

urlpatterns = [
    path('movie_list/', views.MovieListAPIVIEW.as_view()),
    path('movie_detail/<int:pk>/', views.MovieDetailAPIView.as_view()),
    path('movie_create/',views.MovieCreateAPIView.as_view()),
    path('movie_update/<int:pk>/', views.MovieUpdateAPIView.as_view()),
    path('movie_delete/<int:pk>/', views.MovieDestroyAPIView.as_view()),
    path('actor_list/', views.ActorListAPIView.as_view())
]
