import os
import shutil

SOURCE_DIR = "C:/Users/<user>/Pictures/iCloud Photos"
DEST_DIR = "C:/Users/<user>/OneDrive/Images/ICloud"

EXTENSIONS = ['.mp4', '.mov', '.MP4', '.MOV']

for dirpath, dirnames, filenames in os.walk(SOURCE_DIR):
	for filename in filenames:
		if any(filename.endswith(ext) for ext in EXTENSIONS):

			source_file = os.path.join(dirpath, filename)
			dest_file = os.path.join(DEST_DIR, filename)

			# skip if already exists
			if os.path.exists(dest_file):
				print(f"Skipping {filename} as it already exists in the destination directory")
				continue

			# copy file
			print(f"Copying {source_file} to {dest_file}")
			shutil.copy2(source_file, dest_file)

print("Copying process completed successfully!")