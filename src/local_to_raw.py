import os
import shutil

source_file = "game_logs.json"
raw_dir = "data/raw"
destination_file = os.path.join(raw_dir, "game_logs.json")

os.makedirs(raw_dir, exist_ok=True)  # Create folder if it doesn’t exist
if os.path.exists(source_file):
    shutil.move(source_file, destination_file)
    print(f"Moved {source_file} to {destination_file}")
else:
    print(f"Error: {source_file} not found")