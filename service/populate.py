import os
import django
from datetime import date

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "service.settings")
django.setup()

from streaming.models import Favourite, Movie, MovieWatched, User

print('Starting populate script')

# Remove existing data
print('- Removing existing data')
User.objects.all().delete()
Movie.objects.all().delete()
Favourite.objects.all().delete()
MovieWatched.objects.all().delete()


# Generate some users
print('- Generating some user')
User.objects.create(
    username='pedro.carvalho',
    email='pedro@mail.com',
    first_name='Pedro',
    last_name='Carvalho',
    birth_date=date(1987, 4, 17),
)
User.objects.create(
    username='jorge.campos',
    email='jorge@mail.com',
    first_name='Jorge',
    last_name='Campos',
    birth_date=date(1992, 11, 5),
)
User.objects.create(
    username='julia.martins',
    email='julia@mail.com',
    first_name='Julia',
    last_name='Martins',
    birth_date=date(1989, 7, 23),
    type=User.Type.ADMIN
)
for user in User.objects.all():
    user.set_password('fgv123')
    user.save()

# Generate some movies
print('- Generating some movies')
Movie.objects.create(
    title='The Shawshank Redemption',
    year=1994,
    cover='https://m.media-amazon.com/images/M/MV5BMDFkYTc0MGEtZmNhMC00ZDIzLWFmNTEtODM1ZmRlYWMwMWFmXkEyXkFqcGdeQXVy'
          'MTMxODk2OTU@._V1_UY400_CR0,0,270,400_AL_.jpg',
    description='Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts '
                'of common decency.',
    midia='https://www.youtube.com/embed/PLl99DlL6b4'
)
Movie.objects.create(
    title='The Godfather',
    year=1972,
    cover='https://m.media-amazon.com/images/M/MV5BM2MyNjYxNmUtYTAwNi00MTYxLWJmNWYtYzZlODY3ZTk3OTFlXkEyXkFqcGdeQXVyN'
          'zkwMjQ5NzM@._V1_UY400_CR1,0,280,400_AL_.jpg',
    description='The aging patriarch of an organized crime dynasty in postwar New York City transfers control of his '
                'clandestine empire to his reluctant youngest son.',
    midia='https://www.youtube.com/embed/UaVTIH8mujA'
)
Movie.objects.create(
    title='The Dark Knight',
    year=2008,
    cover='https://m.media-amazon.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_UY400_CR0,0,270,'
          '400_AL_.jpg',
    description='When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept '
                'one of the greatest psychological and physical tests of his ability to fight injustice.',
    midia='https://www.youtube.com/embed/kmJLuwP3MbY'
)
Movie.objects.create(
    title='The Lord of the Rings: The Return of the King',
    year=2003,
    cover='https://m.media-amazon.com/images/M/MV5BNzA5ZDNlZWMtM2NhNS00NDJjLTk4NDItYTRmY2EwMWZlMTY3XkEyXkFqcGdeQXVyN'
          'zkwMjQ5NzM@._V1_UY400_CR0,0,270,400_AL_.jpg',
    description='Gandalf and Aragorn lead the World of Men against Sauron\'s army to draw his gaze from Frodo and Sam '
                'as they approach Mount Doom with the One Ring.',
    midia='https://www.youtube.com/embed/zckJCxYxn1g'
)
Movie.objects.create(
    title='Pulp Fiction',
    year=1994,
    cover='https://m.media-amazon.com/images/M/MV5BNGNhMDIzZTUtNTBlZi00MTRlLWFjM2ItYzViMjE3YzI5MjljXkEyXkFqcGdeQXVyNz'
          'kwMjQ5NzM@._V1_UY400_CR0,0,270,400_AL_.jpg',
    description='The lives of two mob hitmen, a boxer, a gangster and his wife, and a pair of diner bandits intertwine '
                'in four tales of violence and redemption.',
    midia='https://www.youtube.com/embed/tGpTpVyI_OQ'
)
Movie.objects.create(
    title='Forrest Gump',
    year=1994,
    cover='https://m.media-amazon.com/images/M/MV5BNWIwODRlZTUtY2U3ZS00Yzg1LWJhNzYtMmZiYmEyNmU1NjMzXkEyXkFqcGdeQXVyMT'
          'QxNzMzNDI@._V1_UY400_CR0,0,270,400_AL_.jpg',
    description='The presidencies of Kennedy and Johnson, the Vietnam War, the Watergate scandal and other historical '
                'events unfold from the perspective of an Alabama man with an IQ of 75, whose only desire is to be '
                'reunited with his childhood sweetheart.',
    midia='https://www.youtube.com/embed/bLvqoHBptjg'
)
Movie.objects.create(
    title='Inception',
    year=2010,
    cover='https://m.media-amazon.com/images/M/MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@._V1_UY400_CR0,0,'
          '270,400_AL_.jpg',
    description='A thief who steals corporate secrets through the use of dream-sharing technology is given the '
                'inverse task of planting an idea into the mind of a C.E.O., but his tragic past may doom the project '
                'and his team to disaster.',
    midia='https://www.youtube.com/embed/hstBN0Qkqhc'
)
Movie.objects.create(
    title='The Matrix',
    year=1999,
    cover='https://m.media-amazon.com/images/M/MV5BNzQzOTk3OTAtNDQ0Zi00ZTVkLWI0MTEtMDllZjNkYzNjNTc4L2ltYWdlXkEyXkFqc'
          'GdeQXVyNjU0OTQ0OTY@._V1_UY400_CR0,0,260,400_AL_.jpg',
    description='When a beautiful stranger leads computer hacker Neo to a forbidding underworld, he discovers the '
                'shocking truth--the life he knows is the elaborate deception of an evil cyber-intelligence.',
    midia='https://www.youtube.com/embed/nUEQNVV3Gfs'
)
Movie.objects.create(
    title='Saving Private Ryan',
    year=1998,
    cover='https://m.media-amazon.com/images/M/MV5BZjhkMDM4MWItZTVjOC00ZDRhLThmYTAtM2I5NzBmNmNlMzI1XkEyXkFqcGdeQXVy'
          'NDYyMDk5MTU@._V1_UY400_CR0,0,270,400_AL_.jpg',
    description='Following the Normandy Landings, a group of U.S. soldiers go behind enemy lines to retrieve a '
                'paratrooper whose brothers have been killed in action.',
    midia='https://www.youtube.com/embed/9CiW_DgxCnQ'
)
Movie.objects.create(
    title='Star Wars: Episode IV - A New Hope',
    year=1977,
    cover='https://m.media-amazon.com/images/I/612h-jwI+EL._AC_UF1000,1000_QL80_.jpg',
    description='Luke Skywalker joins forces with a Jedi Knight, a cocky pilot, a Wookiee and two droids to save the '
                'galaxy from the Empire\'s world-destroying battle station, while also attempting to rescue Princess '
                'Leia from the mysterious Darth Vader.',
    midia='https://www.youtube.com/embed/vZ734NWnAHA'
)

# Create some favourite movies for each user
print('- Creating favourite movies for each user')
for user in User.objects.all():
    from random import randint
    num_favourite_movies = randint(1, 3)
    movies = Movie.objects.order_by('?')[:num_favourite_movies]
    for movie in movies:
        Favourite.objects.create(
            user=user,
            movie=movie
        )

print('Finished!')
