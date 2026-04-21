from timetable import load_modules, create_all_sessions, create_random_timetable
from fitness import count_clashes, count_staff_days, evaluate_timetable

def main():
    modules = load_modules("data/modules.txt")
    sessions = create_all_sessions(modules)
    timetable = create_random_timetable(modules)

    # print("Loaded modules:\n")
    # for module_id, info in modules.items():
    #     print(f"{module_id}: {info}")

    # print("All sessions:")
    # for session in sessions:
    #     print(session)

    print("Random timetable:\n")
    for session, timeslot in timetable.items():
        print(f"{session} -> {timeslot}")

    # clashes = count_clashes(timetable, modules)
    # staff_days = count_staff_days(timetable, modules)
    clashes, staff_days = evaluate_timetable(timetable, modules)

    print("\nObjective values:")
    print(f"Clashes: {clashes}")
    print(f"Staff teaching days: {staff_days}")

if __name__ == "__main__":
    main()