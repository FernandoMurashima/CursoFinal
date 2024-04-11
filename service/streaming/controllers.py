from .models import Favourite, Movie


def list_movies():
    """
    List all movies in the catalog.

    :return: queryset with all movies
    """
    movies = []
    for movie in Movie.objects.all():
        movies.append({
            'id': movie.id,
            'title': movie.title,
            'year': movie.year
        })
    return movies


def is_movie_favourite(movie, user):
    """
    List all films marked as favourite for a given user.

    :param movie: instance of Movie
    :param user: instance of User
    :return: True if the movie is favourite for the user
    """
    return Favourite.objects.filter(user=user, movie=movie).count() != 0


def mark_movie_as_favourite(movie, state, user):
    """
    Set or unset a movie as favourite for the given user.

    :param movie: instance of Movie
    :param state: True if should be favourite
    :param user: instance of User
    """
    if state:
        Favourite.objects.get_or_create(
            movie=movie,
            user=user
        )
    else:
        Favourite.objects.filter(
            movie=movie,
            user=user
        ).delete()
