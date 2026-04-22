from population import (
    build_evaluated_population,
    create_offspring_population,
    combine_and_select_pareto,
    refill_population,
)

def run_simple_optimizer(modules, population_size=10, generations=10):
    # first simple multi-objective evolutionary optimiser
    population = build_evaluated_population(modules, population_size)
    history = []

    for generation in range(generations):
        offspring = create_offspring_population(population, modules)
        survivors = combine_and_select_pareto(population, offspring)

        history.append([ind["objectives"] for ind in survivors])

        population = refill_population(survivors, modules, population_size)

    return population, history