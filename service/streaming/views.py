from django.contrib.auth import get_user_model

from rest_framework import views, viewsets
from rest_framework import permissions
from rest_framework.exceptions import APIException
from rest_framework.response import Response

from .controllers import is_movie_favourite, list_movies, mark_movie_as_favourite
from .serializers import FavouriteSerializer, MovieSerializer, MovieWatchedSerializer, UserSerializer
from .models import Favourite, Movie, MovieWatched


class UserViewSet(viewsets.ModelViewSet):
    """
    User viewset.
    """
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class MovieViewSet(viewsets.ModelViewSet):
    """
    Movie viewset.
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [permissions.IsAuthenticated]


class FavouriteViewSet(viewsets.ModelViewSet):
    """
    Favourite viewset.
    """
    queryset = Favourite.objects.all()
    serializer_class = FavouriteSerializer
    permission_classes = [permissions.IsAuthenticated]


class MovieWatchedViewSet(viewsets.ModelViewSet):
    """
    MovieWatched viewset.
    """
    queryset = MovieWatched.objects.all()
    serializer_class = MovieWatchedSerializer
    permission_classes = [permissions.IsAuthenticated]


class MovieView(views.APIView):
    """
    Movies view
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        movies = list_movies()
        return Response(movies)


class FavouriteView(views.APIView):
    """
    Favourite view
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        """
        Check if a given movie is favourite
        """
        # Get the movie
        if 'id' not in request.GET:
            raise APIException('The `id` must be informed')
        movie_id = request.GET['id']
        movie = Movie.objects.get(id=movie_id)

        # Check if is favourite
        is_favourite = is_movie_favourite(movie, request.user)

        # Return the response data
        response_data = {
            'is_favourite': is_favourite
        }
        return Response(response_data)

    def post(self, request, *args, **kwargs):
        """
        Mark a movie as favourite (or not).
        """
        # Get the movie
        if 'id' not in request.POST:
            raise APIException('The `id` must be informed')
        movie_id = request.POST['id']
        movie = Movie.objects.get(id=movie_id)

        # Get the desired state
        if 'state' not in request.POST:
            raise APIException('The `state` must be informed')
        state = request.POST['state'] == 'true'

        # Mark as favourite
        mark_movie_as_favourite(movie, state, request.user)

        # Return the response
        return Response({})
