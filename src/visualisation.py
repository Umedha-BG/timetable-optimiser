import matplotlib.pyplot as plt

def plot_pareto_front(pareto_front):
    # clashes on the x-axis, staff teaching days on y-axis
    clashes = [individual["objectives"][0] for individual in pareto_front]
    staff_days = [individual["objectives"][1] for individual in pareto_front]

    plt.figure(figsize=(8, 6))
    plt.scatter(clashes, staff_days)

    plt.xlabel("Clashes")
    plt.ylabel("Staff teaching days")
    plt.title("Pareto Front for Timetable Optimisation")
    plt.grid(True)

    plt.show()