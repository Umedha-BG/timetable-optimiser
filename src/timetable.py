import random

def normalise_module_code(code):
    # formatting issue fix in module codes
    code = code.strip().upper()
    code = code.replace("M0D", "MOD")
    
    if code.startswith("MOD"):
        suffix = code[3:]
        if suffix.isdigit() and len(suffix) == 2:
            code = f"MOD0{suffix}"

    return code


def load_modules(filename):
    modules = {}

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue

            parts = line.split("|")

            module_id = normalise_module_code(parts[0])
            lecturer = parts[1].strip()
            lab_count = int(parts[2].strip())

            if len(parts) > 3 and parts[3].strip():
                conflicts = [normalise_module_code(item) for item in parts[3].split(",")]
            else:
                conflicts = []

            modules[module_id] = {
                "lecturer": lecturer,
                "lab_count": lab_count,
                "conflicts": conflicts,
            }

    return modules


DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri"]
SLOTS = [0, 1, 2, 3]


def create_all_sessions(modules):
    #list for all sessions that must be scheduled
    sessions = []

    for module_id, info in modules.items():
        sessions.append((module_id, "lecture", 0))
        
        for lab_number in range(1, info["lab_count"] + 1):
            sessions.append((module_id, "lab", lab_number))

    return sessions

def random_timeslot():
    # individual random day/slot pair
    day = random.choice(DAYS)
    slot = random.choice(SLOTS)
    return (day, slot)


def create_random_timetable(modules):
    # first random timetable
    sessions = create_all_sessions(modules)
    timetable = {}

    for session in sessions:
        timetable[session] = random_timeslot()

    return timetable