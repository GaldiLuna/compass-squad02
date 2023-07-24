def etapa4():
    movie_frequency = {}
    with open("actors.csv", "r") as file:
        lines = file.readlines()
        for line in lines[1:]:
            _, _, _, _, _, _, movies = line.strip().split(";")
            movies = movies.split(",")
            for movie in movies:
                movie_frequency[movie] = movie_frequency.get(movie, 0) + 1

    max_frequency = max(movie_frequency.values())
    most_frequent_movies = [
        movie for movie, freq in movie_frequency.items() if freq == max_frequency
    ]

    with open("etapa-4.txt", "w") as file:
        file.write(f"{','.join(most_frequent_movies)};{max_frequency}")


if __name__ == "__main__":
    etapa4()
