def etapa1():
    actor_movies = {}
    with open("actors.csv", "r") as file:
        lines = file.readlines()
        for line in lines[1:]:
            actor, _, _, _, _, _, movies = line.strip().split(";")
            num_movies = len(movies.split(","))
            actor_movies[actor] = num_movies

    max_movies_actor = max(actor_movies, key=actor_movies.get)
    max_movies_count = actor_movies[max_movies_actor]

    with open("etapa-1.txt", "w") as file:
        file.write(f"{max_movies_actor};{max_movies_count}")


if __name__ == "__main__":
    etapa1()
