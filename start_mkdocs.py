from pathlib import Path
import shutil
import subprocess
import sys


def main() -> None:
    project_root = Path(__file__).resolve().parent

    # Prefer mkdocs on PATH, fallback to python -m mkdocs in active venv.
    if shutil.which("mkdocs"):
        command = ["mkdocs", "serve"]
    else:
        command = [sys.executable, "-m", "mkdocs", "serve"]

    print(f"Starting MkDocs server in: {project_root}")
    print("Press Ctrl+C to stop.")

    try:
        subprocess.run(command, cwd=project_root, check=False)
    except KeyboardInterrupt:
        print("\nMkDocs server stopped.")


if __name__ == "__main__":
    main()
