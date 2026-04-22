from population import (
    build_evaluated_population,
    create_offspring_population,
    combine_and_select_next_generation,
    refill_population,
)

from pareto import get_pareto_front

# def run_simple_optimizer(modules, population_size=10, generations=10):
#     # first simple multi-objective evolutionary optimiser
#     population = build_evaluated_population(modules, population_size)
#     history = []

#     for generation in range(generations):
#         offspring = create_offspring_population(population, modules)
#         survivors = combine_and_select_pareto(population, offspring)

#         history.append([ind["objectives"] for ind in survivors])

#         population = refill_population(survivors, modules, population_size)

#     return population, history

def run_simple_optimizer(modules, population_size=10, generations=10, mutation_rate=0.3):
    # updated multi-objective evolutionary optimiser inspired with NSGA
    population = build_evaluated_population(modules, population_size)
    history = []

    for generation in range(generations):
        offspring = create_offspring_population(
            population,
            modules,
            mutation_rate=mutation_rate
        )

        population = combine_and_select_next_generation(
            population,
            offspring,
            target_size=population_size
        )

        current_front = get_pareto_front(population)
        history.append([ind["objectives"] for ind in current_front])

    return population, history