from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import *
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import *
from .permissios import *
from rest_framework.permissions import *
from .filters import *
from django_filters import rest_framework as filters

from rest_framework.filters import OrderingFilter

######### WITH GENERICS ###################

class MovieListAPIVIEW(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieListSerializer
    permission_classes = [AllowAny]
    filterset_class = MovieFilter 
    ordering_fields = ['title',] 

class ActorListAPIView(generics.ListAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorListSerializer
    permission_classes = [AllowAny]
    filterset_class = ActorFilter

# права админа или тп
class MovieDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieDetailSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_object(self):
        movie = super().get_object()    
        movie.views += 1
        movie.save()
        return movie

class MovieCreateAPIView(generics.CreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieCreateUpdateSerializer
    permission_classes = [IsAuthenticated]

class MovieUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieCreateUpdateSerializer
    permission_classes = [IsOwnerOrReadOnly]

class MovieDestroyAPIView(generics.RetrieveDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieCreateUpdateSerializer
    permission_classes = [IsAdminUser]


######### WITH VIEWSETS ###################

# class MovieViewSet(viewsets.ModelViewSet):
#     queryset = Movie.objects.all()

#     def get_serializer_class(self):
#         if self.action == 'list':
#             return MovieListSerializer
#         elif self.action in ['retrieve', 'update', 'partial_update']:
#             return MovieDetailSerializer
#         elif self.action == 'create':
#             return MovieCreateUpdateSerializer
#         elif self.action == 'destroy':
#             return MovieCreateUpdateSerializer
        

#         @action(methods=['get'], default = True)
#         def genre(self, request, pk=None):
#             genres = Genre.objects.get(pk=pk)
#             return Response({"genres": genres.name})