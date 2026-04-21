from timetable import load_modules, create_all_sessions, create_random_timetable, create_population
from fitness import count_clashes, count_staff_days, evaluate_timetable
from population import build_evaluated_population
from pareto import dominates, get_pareto_front

def main():
    modules = load_modules("data/modules.txt")
    sessions = create_all_sessions(modules)
    timetable = create_random_timetable(modules)
    population = build_evaluated_population(modules, population_size=5)
    pareto_front = get_pareto_front(population)

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

    print("Population size:", len(population))

    for i, individual in enumerate(population, start=1):
        clashes, staff_days = individual["objectives"]
        print(f"Individual {i}: Clashes = {clashes}, Staff days = {staff_days}")

    # print("\nDominance checks:")

    # print("Individual 1 dominate Individual 2?",
    #       dominates(population[0], population[1]))
    # print("Individual 2 dominate Individual 1?",
    #       dominates(population[1], population[0]))

    print("\nPareto Front:\n")

    for individual in pareto_front:
        clashes, staff_days = individual["objectives"]
        print(f"Clashes = {clashes}, Staff days = {staff_days}")


if __name__ == "__main__":
    main()