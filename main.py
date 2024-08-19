import os
import sys


def env_exemplify(path: str) -> None:
    if not os.path.exists(path):
        print("Error: Path not found.")
        sys.exit(1)  # Exit the program with an error code

    with open(path, "r") as file:
        lines = file.readlines()

    modified_lines = []
    for line in lines:
        # Ignore comments and empty lines
        if line.strip() and not line.strip().startswith("#"):
            # Split the line into key and value
            key, _ = line.strip().split("=", 1)
            # Replace the value with an empty string
            modified_lines.append(f'{key}=""\n')
        else:
            modified_lines.append(line)

    # Write the modified lines back to the .env file
    with open(path, "w") as file:
        file.writelines(modified_lines)

    return None
