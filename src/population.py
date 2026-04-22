from timetable import create_population
from fitness import evaluate_timetable
from operators import mutate_timetable
from pareto import get_pareto_front

def build_evaluated_population(modules, population_size):
    # Creating the population where each individual stores the timetable and objective values
    raw_population = create_population(modules, population_size)
    evaluated_population = []

    for timetable in raw_population:
        objectives = evaluate_timetable(timetable, modules)

        individual = {
            "timetable": timetable,
            "objectives": objectives
        }

        evaluated_population.append(individual)

    return evaluated_population


def create_offspring_population(population, modules):
    # mutating each parent timetable once to get offspring
    offspring = []

    for individual in population:
        parent_timetable = individual["timetable"]
        child_timetable = mutate_timetable(parent_timetable)
        child_objectives = evaluate_timetable(child_timetable, modules)

        child = {
            "timetable": child_timetable,
            "objectives": child_objectives
        }

        offspring.append(child)

    return offspring


def combine_and_select_pareto(parents, offspring):
    # Combining parent and offspring populations and return non-dominated individuals.
    combined = parents + offspring
    pareto_front = get_pareto_front(combined)
    return pareto_front


def refill_population(population, modules, target_size):
    # population refill until it reaches target_size.
    new_population = population.copy()

    while len(new_population) < target_size:
        extra_individual = build_evaluated_population(modules, population_size=1)[0]
        new_population.append(extra_individual)

    return new_population