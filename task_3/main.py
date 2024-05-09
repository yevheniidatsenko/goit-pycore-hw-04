import sys
from pathlib import Path
from colorama import init, Fore

# Initializing colorama to support color output
init(autoreset=True)


def display_directory_structure(directory_path, indent=0):
    # Creating a Path object for a given path
    path = Path(directory_path)

    # Checking whether the path exists and is a directory
    if not path.exists() or not path.is_dir():
        print(Fore.RED + f"The path '{directory_path}' does not exist or is not a directory.")
        return

    # Print the name of the current directory
    print(" " * indent + Fore.BLUE + f"📁 {path.name}/")

    # Bypass all subdirectories and files in the current directory
    for item in path.iterdir():
        # Withdrawal of subdirectories
        if item.is_dir():
            print(" " * (indent + 2) + Fore.CYAN + f"📁 {item.name}/")
            display_directory_structure(item, indent + 4)
        # Outputs files
        elif item.is_file():
            print(" " * (indent + 2) + Fore.GREEN + f"📄 {item.name}")


if __name__ == "__main__":
    # Verifying the presence of a command line argument
    if len(sys.argv) != 2:
        print(Fore.RED + "Specify the path to the directory.")
        sys.exit(1)

    # Retrieving the path to a directory from a command line argument
    directory_path = sys.argv[1]

    # Outputting the directory structure
    display_directory_structure(directory_path)