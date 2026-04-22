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