def etapa2():
    actor_gross_revenue = {}
    with open("actors.csv", "r") as file:
        lines = file.readlines()
        for line in lines[1:]:
            actor, _, _, _, _, gross_revenue, _ = line.strip().split(";")
            gross_revenue = float(gross_revenue)
            if actor in actor_gross_revenue:
                actor_gross_revenue[actor].append(gross_revenue)
            else:
                actor_gross_revenue[actor] = [gross_revenue]

    with open("etapa-2.txt", "w") as file:
        for actor, revenue_list in actor_gross_revenue.items():
            avg_revenue = sum(revenue_list) / len(revenue_list)
            file.write(f"{actor};{avg_revenue}\n")


if __name__ == "__main__":
    etapa2()
