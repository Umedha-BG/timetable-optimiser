import matplotlib.pyplot as plt

def plot_pareto_front(pareto_front, save_path=None, show_plot=True):
    unique_points = list(set(ind["objectives"] for ind in pareto_front))

    clashes = [p[0] for p in unique_points]
    staff_days = [p[1] for p in unique_points]

    clashes, staff_days = zip(*sorted(zip(clashes, staff_days)))

    plt.figure(figsize=(8, 6))
    plt.scatter(clashes, staff_days)
    plt.plot(clashes, staff_days)

    plt.xlabel("Clashes")
    plt.ylabel("Staff teaching days")
    plt.title("Pareto Front for Timetable Optimisation")
    plt.grid(True)

    if save_path is not None:
        plt.savefig(save_path, bbox_inches="tight")

    if show_plot:
        plt.show()
    else:
        plt.close()


def plot_pareto_with_population(population, pareto_front, save_path=None, show_plot=True):
    all_clashes = [ind["objectives"][0] for ind in population]
    all_staff = [ind["objectives"][1] for ind in population]

    pareto_points = sorted(set(ind["objectives"] for ind in pareto_front))
    pareto_clashes = [p[0] for p in pareto_points]
    pareto_staff = [p[1] for p in pareto_points]

    plt.figure(figsize=(8, 6))

    # All solutions
    plt.scatter(all_clashes, all_staff, alpha=0.3, label="Final population")

    # Pareto front 
    plt.scatter(pareto_clashes, pareto_staff, label="Pareto front")

    plt.plot(pareto_clashes, pareto_staff)

    plt.xlabel("Clashes")
    plt.ylabel("Staff teaching days")
    plt.title("Final Population and Pareto Front")
    plt.legend()
    plt.grid(True)

    if save_path:
        plt.savefig(save_path, bbox_inches="tight")

    if show_plot:
        plt.show()
    else:
        plt.close()

def plot_convergence(history, save_path=None, show_plot=True):
    best_clashes = []
    best_staff_days = []

    for front in history:
        best_clashes.append(min(point[0] for point in front))
        best_staff_days.append(min(point[1] for point in front))

    generations = range(1, len(history) + 1)

    plt.figure(figsize=(8, 6))
    plt.plot(generations, best_clashes, marker="o", label="Best clashes")
    plt.plot(generations, best_staff_days, marker="o", label="Best staff days")

    plt.xlabel("Generation")
    plt.ylabel("Best objective value")
    plt.title("Convergence Over Generations")
    plt.legend()
    plt.grid(True)

    if save_path:
        plt.savefig(save_path, bbox_inches="tight")

    if show_plot:
        plt.show()
    else:
        plt.close()


def plot_parameter_comparison(results, save_path=None, show_plot=True):
    labels = []
    best_clashes = []
    best_staff_days = []

    for row in results:
        labels.append(
            f"P{row['population_size']}\n"
            f"G{row['generations']}\n"
            f"M{row['mutation_rate']}\n"
            f"S{row['seed']}"
        )
        best_clashes.append(row["best_clashes"])
        best_staff_days.append(row["best_staff_days"])

    x = range(len(results))

    plt.figure(figsize=(12, 6))
    plt.plot(x, best_clashes, marker="o", label="Best clashes")
    plt.plot(x, best_staff_days, marker="o", label="Best staff days")

    plt.xticks(x, labels, rotation=45, ha="right")
    plt.xlabel("Experiment configuration")
    plt.ylabel("Best objective value")
    plt.title("Experiment Comparison")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    if save_path:
        plt.savefig(save_path, bbox_inches="tight")

    if show_plot:
        plt.show()
    else:
        plt.close()
    