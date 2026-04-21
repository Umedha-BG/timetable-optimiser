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