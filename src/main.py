from timetable import load_modules

def main():
    modules = load_modules("data/modules.txt")

    print("Loaded modules:\n")

    for module_id, info in modules.items():
        print(f"{module_id}: {info}")


if __name__ == "__main__":
    main()