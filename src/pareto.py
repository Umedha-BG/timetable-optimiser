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