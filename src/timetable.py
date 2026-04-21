def load_modules(filename):
    modules = {}

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue

            parts = line.split("|")

            module_id = parts[0].strip()
            lecturer = parts[1].strip()
            lab_count = int(parts[2].strip())

            if len(parts) > 3 and parts[3].strip():
                conflicts = [item.strip() for item in parts[3].split(",")]
            else:
                conflicts = []

            modules[module_id] = {
                "lecturer": lecturer,
                "lab_count": lab_count,
                "conflicts": conflicts,
            }

    return modules