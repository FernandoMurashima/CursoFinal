from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Favourite, Movie, MovieWatched


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
    User serializer.
    """
    class Meta:
        model = get_user_model()
        fields = ['url', 'username', 'email', 'type', 'first_name', 'last_name', 'birth_date', 'address']


class MovieSerializer(serializers.HyperlinkedModelSerializer):
    """
    Movie serializer
    """
    class Meta:
        model = Movie
        fields = ['url', 'id', 'title', 'year', 'cover', 'description', 'midia']


class FavouriteSerializer(serializers.HyperlinkedModelSerializer):
    """
    Favourite serializer
    """
    user_id = serializers.IntegerField(source='user.id', read_only=True)
    movie_id = serializers.IntegerField(source='movie.id', read_only=True)

    class Meta:
        model = Favourite
        fields = ['url', 'id', 'user', 'user_id', 'movie', 'movie_id']


class MovieWatchedSerializer(serializers.HyperlinkedModelSerializer):
    """
    Movie watched serializer
    """
    class Meta:
        model = MovieWatched
        fields = ['url', 'id', 'user', 'movie', 'date']
