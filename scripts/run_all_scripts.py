import subprocess
import os

# --- paths ---
scripts_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "scripts"))
script_files = [
    "generate_data.py",
    "build_features.py",
    "normalize_values.py",
    "dimensions.py",
    "visuals.py"
]

# --- run each ---
for script in script_files:
    script_path = os.path.join(scripts_dir, script)
    print(f"\nrunning {script}...")
    result = subprocess.run(["python3", script_path], capture_output=True, text=True)

    if result.returncode == 0:
        print(result.stdout)
    else:
        print(f"Error in {script}:")
        print(result.stderr)
        break  # stop on first failure