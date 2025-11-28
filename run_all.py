import os
import subprocess
import sys
main_folder = r"C:\Users\tinsa\Downloads\RealRTI_modelfiles\RealRTI_modelfiles"

for sub in os.listdir(main_folder):
    sub_folder = os.path.join(main_folder, sub)
    if not os.path.isdir(sub_folder):
        continue

    model_file = os.path.join(sub_folder, "outputs")
    light_file = os.path.join(sub_folder, "test", "dirs.lp")

    # Skip if required files do not exist
    if not (os.path.exists(model_file) and os.path.exists(light_file) ):
        print(f"Skipping {sub_folder} — missing files")
        continue

    print(f"Running test for: {sub_folder}")

    subprocess.call([
        sys.executable, "test.py",
        "--model_path", model_file,
        "--light_path", light_file,
    ])
