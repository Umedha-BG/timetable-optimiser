import csv
import os
import random

from timetable import load_modules
from optimizer import run_simple_optimizer
from pareto import get_pareto_front
from visualisation import plot_pareto_front


def run_experiment(modules, population_size, generations, mutation_rate, seed):
    random.seed(seed)

    final_population, history = run_simple_optimizer(
        modules,
        population_size=population_size,
        generations=generations,
        mutation_rate=mutation_rate,
    )

    final_front = get_pareto_front(final_population)
    final_front.sort(key=lambda x: x["objectives"][0])

    unique_points = sorted(set(ind["objectives"] for ind in final_front))

    best_clashes = min(point[0] for point in unique_points)
    best_staff_days = min(point[1] for point in unique_points)
    pareto_front_size = len(unique_points)

    return {
        "population_size": population_size,
        "generations": generations,
        "mutation_rate": mutation_rate,
        "seed": seed,
        "best_clashes": best_clashes,
        "best_staff_days": best_staff_days,
        "pareto_front_size": pareto_front_size,
        "pareto_points": unique_points,
        "final_front": final_front,
        "history": history,
    }


def save_results_to_csv(results, csv_path):
    file_exists = os.path.isfile(csv_path)
    fieldnames = [
        "population_size",
        "generations",
        "mutation_rate",
        "seed",
        "best_clashes",
        "best_staff_days",
        "pareto_front_size",
        "pareto_points",
        "plot_filename",
    ]

    with open(csv_path, "a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        if not file_exists:
            writer.writeheader()

        for row in results:
            writer.writerow(row)


def main():
    os.makedirs("results", exist_ok=True)
    os.makedirs("results/plots", exist_ok=True)
    seeds = [10, 20, 30, 40, 50]

    modules = load_modules("data/modules.txt")

    experiment_setups = [
    {"population_size": 20, "generations": 20, "mutation_rate": 0.3},
    {"population_size": 50, "generations": 20, "mutation_rate": 0.3},
    {"population_size": 50, "generations": 50, "mutation_rate": 0.3},
    {"population_size": 50, "generations": 20, "mutation_rate": 0.1},
    {"population_size": 50, "generations": 20, "mutation_rate": 0.5},
]
    all_results = []
    for seed in seeds:
        for setup in experiment_setups:
            result = run_experiment(
                modules,
                population_size=setup["population_size"],
                generations=setup["generations"],
                mutation_rate=setup["mutation_rate"],
                seed=seed,
            )

            plot_filename = (
                f"pareto_pop{setup['population_size']}"
                f"_gen{setup['generations']}"
                f"_mut{str(setup['mutation_rate']).replace('.', '_')}"
                f"_seed{seed}.png"
            )
            plot_path = os.path.join("results", "plots", plot_filename)

            plot_pareto_front(result["final_front"], save_path=plot_path, show_plot=False)

            row = {
                "population_size": result["population_size"],
                "generations": result["generations"],
                "mutation_rate": result["mutation_rate"],
                "seed": seed,
                "best_clashes": result["best_clashes"],
                "best_staff_days": result["best_staff_days"],
                "pareto_front_size": result["pareto_front_size"],
                "pareto_points": result["pareto_points"],
                "plot_filename": plot_filename,
            }

            all_results.append(row)

            print(
                f"Done: pop={result['population_size']}, "
                f"gen={result['generations']}, "
                f"mut={result['mutation_rate']}, "
                f"seed={result['seed']}"
            )

    save_results_to_csv(all_results, "results/experiment_results.csv")

if __name__ == "__main__":
    main()