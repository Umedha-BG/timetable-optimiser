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


def plot_pareto_with_population(population, pareto_front):
    all_clashes = [ind["objectives"][0] for ind in population]
    all_staff = [ind["objectives"][1] for ind in population]

    pareto_points = list(set(ind["objectives"] for ind in pareto_front))
    pareto_clashes = [p[0] for p in pareto_points]
    pareto_staff = [p[1] for p in pareto_points]

    plt.figure(figsize=(8, 6))

    # All solutions
    plt.scatter(all_clashes, all_staff, alpha=0.3)

    # Pareto front 
    plt.scatter(pareto_clashes, pareto_staff)

    plt.xlabel("Clashes")
    plt.ylabel("Staff teaching days")
    plt.title("Pareto Front (Highlighted) vs All Solutions")
    plt.grid(True)

    plt.show()