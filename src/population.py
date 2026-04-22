import random
from timetable import create_population
from fitness import evaluate_timetable
from operators import mutate_timetable, crossover_timetables
from pareto import  non_dominated_sort

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


def create_offspring_population(population, modules, mutation_rate=0.3):
    #offspring using crossover and occasional mutation.
    offspring = []
    target_size = len(population)

    while len(offspring) < target_size:
        parent_a = random.choice(population)
        parent_b = random.choice(population)

        child_timetable = crossover_timetables(
            parent_a["timetable"],
            parent_b["timetable"]
        )

        if random.random() < mutation_rate:
            child_timetable = mutate_timetable(child_timetable)

        child_objectives = evaluate_timetable(child_timetable, modules)

        child = {
            "timetable": child_timetable,
            "objectives": child_objectives
        }

        offspring.append(child)

    return offspring


def combine_and_select_next_generation(parents, offspring, target_size):
    # Combine parent and offspring populations and select next gen using non-dominated sorting
    combined = parents + offspring
    fronts = non_dominated_sort(combined)

    next_generation = []

    for front in fronts:
        if len(next_generation) + len(front) <= target_size:
            next_generation.extend(front)
        else:
            remaining_slots = target_size - len(next_generation)
            next_generation.extend(front[:remaining_slots])
            break

    return next_generation


def refill_population(population, modules, target_size):
    # population refill until it reaches target_size.
    new_population = population.copy()

    while len(new_population) < target_size:
        extra_individual = build_evaluated_population(modules, population_size=1)[0]
        new_population.append(extra_individual)

    return new_population