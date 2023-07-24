def etapa3():
    actor_avg_revenue = {}
    with open("actors.csv", "r") as file:
        lines = file.readlines()
        for line in lines[1:]:
            actor, _, _, _, _, gross_revenue, movies = line.strip().split(";")
            gross_revenue = float(gross_revenue)
            num_movies = len(movies.split(","))
            avg_revenue = gross_revenue / num_movies
            actor_avg_revenue[actor] = avg_revenue

    max_avg_actor = max(actor_avg_revenue, key=actor_avg_revenue.get)
    max_avg_revenue = actor_avg_revenue[max_avg_actor]

    with open("etapa-3.txt", "w") as file:
        file.write(f"{max_avg_actor};{max_avg_revenue}")


if __name__ == "__main__":
    etapa3()
