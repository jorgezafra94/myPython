def insert_movie(movies):
    title = input("Enter the movie tittle: ")
    director = input("Enter the director name: ")
    year = input("Enter the year of release: ")
    movie_info = {
        "title": title.capitalize(),
        "director": director.capitalize(),
        "year": year
    }
    movies.append(movie_info)
    print("movie added successfully")

def list_movies(movies):
    for movie in movies:
        print(movie)

def find_movie(movies):
    movie_to_find = input("Enter the title of the movie you want to find: ")
    for movie in movies:
        if movie.get("title") == movie_to_find.capitalize():
            print(movie)
            break
    else:
        print("You dont have that movie in your collection")

movies = []

menu = """
WHAT WOULD YOU LIKE TO DO?
(i) Insert a new Movie
(l) List the movies that you have in your collection
(f) Find a movie by its tittle name
(q) Quit the programm: 
"""

options = {
    "i": insert_movie,
    "l": list_movies,
    "f": find_movie
}

def movie_app():
    while(True):
        user_option = input(menu)
        if user_option == 'q':
            print("bye!")
            break
        elif user_option not in options.keys():
            print("Invalid option!, please try again!")
        else:
            options.get(user_option)(movies)

movie_app()
