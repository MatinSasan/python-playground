from movie import Movie
from user import User

user = User('Mat')

my_movie = Movie("Matrix", "Sci-Fi")

user.movies.append(my_movie)

print(user, user.movies)
