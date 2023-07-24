def etapa5():
    actor_total_gross_revenue = {}
    with open("actors.csv", "r") as file:
        lines = file.readlines()
        for line in lines[1:]:
            actor, _, _, _, _, gross_revenue, _ = line.strip().split(";")
            gross_revenue = float(gross_revenue)
            if actor in actor_total_gross_revenue:
                actor_total_gross_revenue[actor] += gross_revenue
            else:
                actor_total_gross_revenue[actor] = gross_revenue

    sorted_actors = sorted(
        actor_total_gross_revenue.items(), key=lambda x: x[1], reverse=True
    )

    with open("etapa-5.txt", "w") as file:
        for actor, total_revenue in sorted_actors:
            file.write(f"{actor};{total_revenue}\n")


if __name__ == "__main__":
    etapa5()
