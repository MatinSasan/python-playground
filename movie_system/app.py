from movie import Movie
from user import User
import json

user = User('Mat')
user.add_movie('Matrix', 'Sci-Fi')
user.add_movie('The Interview', 'Comedy')


# user.save_to_file()

# my_movie = Movie("Matrix", "Sci-Fi", False)

# user.movies.append(my_movie)

# print(user, user.movies, user.watched_movies())


# user = User.load_from_file('Mat.txt')

# print(user.name, user.movies)

# print(user.json())

with open('my_file.txt', 'w') as f:
    json.dump(user.json(), f)
