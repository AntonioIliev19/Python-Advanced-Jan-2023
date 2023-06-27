def movie_organizer(*movie_and_genre):
    movies_genres = {}
    for movie_name, genre in movie_and_genre:
        if genre not in movies_genres:
            movies_genres[genre] = []
        movies_genres[genre].append(movie_name)  # ADD GENRE IN DICTIONARY

    sorted_genres = sorted(movies_genres.items(), key=lambda x: (-len(x[1]), x[0]))  # SORT GENRES IN DESCENDING ORDER,
    # x[0] = genre IF SAME GENRE ARE 2 OR MORE, RETURN THEM IN ASCENDING ORDER BY GENRE
    # x[1] = number of movies in 1 genre
    result = ""
    for genre, movie_name in sorted_genres:
        sorted_movies = sorted(movie_name)          # sorted in ascending order (alphabetically) by the movie's name.
        result += f"{genre} - {len(sorted_movies)}\n"
        for name in sorted_movies:
            result += f"* {name}\n"
    return result.strip()


print(movie_organizer(
    ("Avatar: The Way of Water", "Action"),
    ("House Of Gucci", "Drama"),
    ("Top Gun", "Action"),
    ("Ted", "Comedy"),
    ("Duck Soup", "Comedy"),
    ("The Dark Knight", "Action"),
    ("A Star Is Born", "Musicals"),
    ("The Warrior", "Action"),
    ("Like A Boss", "Comedy"),
    ("The Green Mile", "Drama"),
    ("21 Jump Street", "Comedy"))
)
