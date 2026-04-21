from timetable import load_modules, create_all_sessions

def main():
    modules = load_modules("data/modules.txt")
    sessions = create_all_sessions(modules)

    # print("Loaded modules:\n")
    # for module_id, info in modules.items():
    #     print(f"{module_id}: {info}")

    print("All sessions:")
    for session in sessions:
        print(session)


if __name__ == "__main__":
    main()