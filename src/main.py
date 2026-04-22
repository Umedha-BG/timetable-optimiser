from timetable import load_modules
from pareto import get_pareto_front
from optimizer import run_simple_optimizer
from visualisation import plot_pareto_front

def main():
    modules = load_modules("data/modules.txt")

    final_population, history = run_simple_optimizer(
        modules,
        population_size=50,
        generations=20
    )

    final_front = get_pareto_front(final_population)
    final_front.sort(key=lambda x: x["objectives"][0])

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