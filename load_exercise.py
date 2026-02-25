import msvcrt
import os
import shutil
import sys


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def get_exercises(exercises_dir):
    if not os.path.exists(exercises_dir):
        return []

    return [
        d
        for d in os.listdir(exercises_dir)
        if os.path.isdir(os.path.join(exercises_dir, d))
    ]


def display_menu(exercises, selected_index):
    clear_screen()
    print("\033[1;36m=== Select an Exercise to Load ===\033[0m\n")

    if not exercises:
        print("\033[1;33mNo exercises found in the 'exercises' folder.\033[0m")
        print("\nPress any key to exit...")
        return

    for i, exercise in enumerate(exercises):
        if i == selected_index:
            print(f"\033[1;32m> {exercise}\033[0m")
        else:
            print(f"  {exercise}")

    print(
        "\n\033[1;30mUse Up/Down arrows to navigate, Enter to select, 'q' or Esc to quit.\033[0m"
    )


def copy_files(exercise_path):
    # Files to copy
    files_to_copy = ["main.py", "test_main.py"]
    success = True

    for file in files_to_copy:
        src = os.path.join(exercise_path, file)
        dst = os.path.join(".", file)

        if os.path.exists(src):
            try:
                shutil.copy2(src, dst)
                print(f"\033[1;32mSuccessfully copied {file}\033[0m")
            except Exception as e:
                print(f"\033[1;31mError copying {file}: {e}\033[0m")
                success = False
        else:
            print(f"\033[1;33mWarning: {file} not found in {exercise_path}\033[0m")
            success = False

    return success


def main():
    # Enable ANSI escape sequences on Windows
    os.system("")

    exercises_dir = "exercises"
    exercises = get_exercises(exercises_dir)

    selected_index = 0

    while True:
        display_menu(exercises, selected_index)

        if not exercises:
            msvcrt.getch()
            break

        # Get keypress
        key = msvcrt.getch()

        # Check for special keys (arrows are prefix \xe0 or \x00)
        if key in (b"\xe0", b"\x00"):
            key = msvcrt.getch()
            if key == b"H":  # Up arrow
                selected_index = max(0, selected_index - 1)
            elif key == b"P":  # Down arrow
                selected_index = min(len(exercises) - 1, selected_index + 1)
        elif key == b"\r":  # Enter
            print(
                f"\n\033[1;36mLoading exercise: {exercises[selected_index]}...\033[0m"
            )
            exercise_path = os.path.join(exercises_dir, exercises[selected_index])
            copy_files(exercise_path)
            print("\nPress any key to exit...")
            msvcrt.getch()
            break
        elif key.lower() == b"q" or key == b"\x1b":  # 'q' or Esc
            break


if __name__ == "__main__":
    main()
