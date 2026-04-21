def count_clashes(timetable, modules):
    # clash count between conflicting modules
    sessions = list(timetable.keys())
    clash_count = 0

    for i in range(len(sessions)):
        session_a = sessions[i]
        module_a = session_a[0]
        timeslot_a = timetable[session_a]

        for j in range(i + 1, len(sessions)):
            session_b = sessions[j]
            module_b = session_b[0]
            timeslot_b = timetable[session_b]

            # Ignore if not in the same timeslot
            if timeslot_a != timeslot_b:
                continue

            # Ignore comparisons within the same module
            if module_a == module_b:
                continue

            # Count clash if module_b is in module_a's conflict list
            if module_b in modules[module_a]["conflicts"]:
                clash_count += 1

    return clash_count

def count_staff_days(timetable, modules):
    # total number of teaching days used by all lecturers count
    lecturer_days = {}

    for session, timeslot in timetable.items():
        module_id = session[0]
        day = timeslot[0]
        lecturer = modules[module_id]["lecturer"]

        if lecturer not in lecturer_days:
            lecturer_days[lecturer] = set()

        lecturer_days[lecturer].add(day)

    total_staff_days = 0
    for days in lecturer_days.values():
        total_staff_days += len(days)

    return total_staff_days