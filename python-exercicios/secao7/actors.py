def ler_arquivo_actors():
    with open("actors.csv", "r") as file:
        lines = file.readlines()
    return lines


def etapa1(lines):
    actor_movies = {}
    for line in lines[1:]:
        actor, _, num_movies, _, _, _, _ = line.strip().split(",")
        num_movies = int(num_movies)
        actor_movies[actor] = num_movies

    max_movies_actor = max(actor_movies, key=actor_movies.get)
    max_movies_count = actor_movies[max_movies_actor]

    return max_movies_actor, max_movies_count


def etapa2(lines):
    actor_gross_revenue = {}
    actor_num_movies = {}
    for line in lines[1:]:
        actor, total_gross, num_movies, _, _, _, _ = line.strip().split(",")
        total_gross = float(total_gross)
        num_movies = int(num_movies)
        actor_gross_revenue[actor] = total_gross
        actor_num_movies[actor] = num_movies

    actor_avg_revenue = {}
    for actor in actor_gross_revenue:
        avg_revenue = actor_gross_revenue[actor] / actor_num_movies[actor]
        actor_avg_revenue[actor] = avg_revenue

    return actor_avg_revenue


def etapa3(lines):
    actor_avg_revenue = {}
    for line in lines[1:]:
        actor, total_gross, num_movies, _, _, _, _ = line.strip().split(",")
        total_gross = float(total_gross)
        num_movies = int(num_movies)
        avg_revenue = total_gross / num_movies
        actor_avg_revenue[actor] = avg_revenue

    max_avg_actor = max(actor_avg_revenue, key=actor_avg_revenue.get)
    max_avg_revenue = actor_avg_revenue[max_avg_actor]

    return max_avg_actor, max_avg_revenue


def etapa4(lines):
    movie_frequency = {}
    for line in lines[1:]:
        _, _, num_movies, _, _, _, movies = line.strip().split(",")
        num_movies = int(num_movies)
        movies = movies.split(",")
        for movie in movies:
            if num_movies > 1:
                movie_frequency[movie] = movie_frequency.get(movie, 0) + 1

    max_frequency = max(movie_frequency.values())
    most_frequent_movies = [
        movie for movie, freq in movie_frequency.items() if freq == max_frequency
    ]

    return most_frequent_movies, max_frequency


def etapa5(lines):
    actor_total_gross_revenue = {}
    for line in lines[1:]:
        actor, total_gross, _, _, _, _, _ = line.strip().split(",")
        total_gross = float(total_gross)
        if actor in actor_total_gross_revenue:
            actor_total_gross_revenue[actor] += total_gross
        else:
            actor_total_gross_revenue[actor] = total_gross

    sorted_actors = sorted(
        actor_total_gross_revenue.items(), key=lambda x: x[1], reverse=True
    )

    return sorted_actors


def main():
    lines = ler_arquivo_actors()

    # Etapa 1
    max_movies_actor, max_movies_count = etapa1(lines)
    print(
        f"O ator/atriz com maior número de filmes é {max_movies_actor} com {max_movies_count} filmes."
    )

    # Etapa 2
    actor_avg_revenue = etapa2(lines)
    for actor, avg_revenue in actor_avg_revenue.items():
        print(
            f"A média de faturamento bruto por filme para o(a) ator/atriz {actor} é {avg_revenue:.2f}."
        )

    # Etapa 3
    max_avg_actor, max_avg_revenue = etapa3(lines)
    print(
        f"O ator/atriz com a maior média de faturamento por filme é {max_avg_actor} com média de {max_avg_revenue:.2f}."
    )

    # Etapa 4
    most_frequent_movies, max_frequency = etapa4(lines)
    print(
        f"O(s) filme(s) mais frequente(s) é(são): {', '.join(most_frequent_movies)} com frequência de {max_frequency}."
    )

    # Etapa 5
    sorted_actors = etapa5(lines)
    print(
        "Lista de atores ordenada pelo faturamento bruto total, em ordem decrescente:"
    )
    for actor, total_revenue in sorted_actors:
        print(f"{actor}: {total_revenue:.2f}")


if __name__ == "__main__":
    main()
