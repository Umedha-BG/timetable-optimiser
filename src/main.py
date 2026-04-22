import random
random.seed(55)

from timetable import load_modules, create_all_sessions, create_random_timetable, create_population
from fitness import count_clashes, count_staff_days, evaluate_timetable
from population import build_evaluated_population, create_offspring_population, combine_and_select_next_generation
from pareto import dominates, get_pareto_front
from operators import mutate_timetable
from optimizer import run_simple_optimizer
from visualisation import plot_pareto_front, plot_pareto_with_population

def main():
    modules = load_modules("data/modules.txt")
    sessions = create_all_sessions(modules)
    timetable = create_random_timetable(modules)
    population = build_evaluated_population(modules, population_size=5)
    pareto_front = get_pareto_front(population)

    original = create_random_timetable(modules)
    mutated = mutate_timetable(original)
    original_objectives = evaluate_timetable(original, modules)
    mutated_objectives = evaluate_timetable(mutated, modules)

    parents = build_evaluated_population(modules, population_size=5)
    offspring = create_offspring_population(parents, modules)
    # survivors = combine_and_select_pareto(parents, offspring)
    survivors = combine_and_select_next_generation(parents, offspring, target_size=5)

    final_population, history = run_simple_optimizer(
        modules,
        population_size=20,
        generations=20
    )

    final_front = get_pareto_front(final_population)

    # print("Loaded modules:\n")
    # for module_id, info in modules.items():
    #     print(f"{module_id}: {info}")

    # print("All sessions:")
    # for session in sessions:
    #     print(session)

    # print("Random timetable:\n")
    # for session, timeslot in timetable.items():
    #     print(f"{session} -> {timeslot}")

    # clashes = count_clashes(timetable, modules)
    # staff_days = count_staff_days(timetable, modules)
    # clashes, staff_days = evaluate_timetable(timetable, modules)

    # print("\nObjective values:")
    # print(f"Clashes: {clashes}")
    # print(f"Staff teaching days: {staff_days}")

    # print("Population size:", len(population))

    # for i, individual in enumerate(population, start=1):
    #     clashes, staff_days = individual["objectives"]
    #     print(f"Individual {i}: Clashes = {clashes}, Staff days = {staff_days}")

    # print("\nDominance checks:")

    # print("Individual 1 dominate Individual 2?",
    #       dominates(population[0], population[1]))
    # print("Individual 2 dominate Individual 1?",
    #       dominates(population[1], population[0]))

    # print("\nPareto Front:\n")

    # for individual in pareto_front:
    #     clashes, staff_days = individual["objectives"]
    #     print(f"Clashes = {clashes}, Staff days = {staff_days}")

    # print("Original timetable objectives:")
    # print(f"Clashes = {original_objectives[0]}, Staff days = {original_objectives[1]}")

    # print("\nMutated timetable objectives:")
    # print(f"Clashes = {mutated_objectives[0]}, Staff days = {mutated_objectives[1]}")

    # print("Parents:\n")
    # for i, individual in enumerate(parents, start=1):
    #     clashes, staff_days = individual["objectives"]
    #     print(f"Parent {i}: Clashes = {clashes}, Staff days = {staff_days}")

    # print("\nOffspring:\n")
    # for i, individual in enumerate(offspring, start=1):
    #     clashes, staff_days = individual["objectives"]
    #     print(f"Child {i}: Clashes = {clashes}, Staff days = {staff_days}")

    # print("\nSelected Pareto survivors:\n")
    # for i, individual in enumerate(survivors, start=1):
    #     clashes, staff_days = individual["objectives"]
    #     print(f"Survivor {i}: Clashes = {clashes}, Staff days = {staff_days}")

    print("Final Pareto front:\n")
    for i, individual in enumerate(final_front, start=1):
        clashes, staff_days = individual["objectives"]
        print(f"Solution {i}: Clashes = {clashes}, Staff days = {staff_days}")

    print("\nPareto front size by generation:\n")
    for generation_index, front in enumerate(history, start=1):
        print(f"Generation {generation_index}: {len(front)} solutions")

    plot_pareto_front(final_front)

if __name__ == "__main__":
    main()