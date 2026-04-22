import random
from copy import deepcopy
from timetable import random_timeslot


def mutate_timetable(timetable):
    # Return a mutated copy of the timetable
    mutated = deepcopy(timetable)

    sessions = list(mutated.keys())
    chosen_session = random.choice(sessions)

    mutated[chosen_session] = random_timeslot()

    return mutated


def crossover_timetables(parent_a, parent_b):
    # Creating one child combining two parent timetables
    child = {}

    for session in parent_a:
        if random.random() < 0.5:
            child[session] = parent_a[session]
        else:
            child[session] = parent_b[session]

    return child