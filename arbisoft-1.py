import urllib.request
import json
with urllib.request.urlopen("https://api.myjson.com/bins/trjyu") as url:
    movies = json.loads(url.read().decode())
    # print(movies)


def filterMovies(genre: str, gross_limit: float):
    selected_movies = []
    for movie in movies:
        if genre in movie["genre"] and float(movie["gross"][1:-2]) <= gross_limit:
            selected_movies.append(movie)
    print(selected_movies, len(selected_movies))

    with open("output.txt", "a") as w:
        w.write(str(len(selected_movies)))
        w.write("\n")


with open("input.txt", "r") as f:
    number_of_inputs = f.readline()
    for i in range(0, int(number_of_inputs)):
        inputs = f.readline()
        genre, gross_limit = inputs.split(',', 1)
        print(
            f"Filtered {genre} movies having gross <= {gross_limit}")
        filterMovies(genre.title(), float(gross_limit))
