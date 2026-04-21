from timetable import create_population
from fitness import evaluate_timetable


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