import os
import sys


def env_exemplify(path: str) -> None:
    if not os.path.exists(path):
        print("Error: Path not found.")
        sys.exit(1)

    with open(path, "r") as file:
        lines = file.readlines()

    modified_lines = []
    for line in lines:
        if line.strip() and not line.strip().startswith("#"):
            key, _ = line.strip().split("=", 1)
            modified_lines.append(f'{key}=""\n')
        else:
            modified_lines.append(line)

    with open(path, "w") as file:
        file.writelines(modified_lines)

    return None  

