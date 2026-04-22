def dominates(individual_a, individual_b):
    #Return True if individual_a dominates individual_b
    objectives_a = individual_a["objectives"]
    objectives_b = individual_b["objectives"]

    no_worse_in_all = True
    strictly_better_in_at_least_one = False

    for a, b in zip(objectives_a, objectives_b):
        if a > b:
            no_worse_in_all = False
            break
        if a < b:
            strictly_better_in_at_least_one = True

    return no_worse_in_all and strictly_better_in_at_least_one


def non_dominated_sort(population):
    # Splitting the population into Pareto fronts.
    working_population = population.copy()
    fronts = []

    while working_population:
        current_front = get_pareto_front(working_population)
        fronts.append(current_front)

        # Remove individuals in the current front from working_population
        current_front_ids = {id(individual) for individual in current_front}
        working_population = [
            individual
            for individual in working_population
            if id(individual) not in current_front_ids
        ]

    return fronts


def get_pareto_front(population):
    # Return the list of non-dominated individuals
    pareto_front = []

    for i, individual_a in enumerate(population):
        dominated = False

        for j, individual_b in enumerate(population):
            if i == j:
                continue

            if dominates(individual_b, individual_a):
                dominated = True
                break

        if not dominated:
            pareto_front.append(individual_a)

    return pareto_front