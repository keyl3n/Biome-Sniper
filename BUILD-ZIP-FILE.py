import os, shutil
import updater, time

from zipfile import ZipFile, ZIP_DEFLATED
from pathlib import Path
import pathspec

print("\nTarget version:", updater.CURRENT, "\n")

print("Clearing existing zips...")
folder = os.path.dirname(os.path.abspath(__file__))
for file in os.listdir(folder):
	if file.endswith(".zip"):
		os.remove(os.path.join(folder, file))
		print("Removed:", file)
if os.path.isdir("build"):
	shutil.rmtree("build")
print("Complete\n")

folder = Path(__file__).parent

# extra files/folders to ignore
custom_exclude = {"data.json", ".gitignore", "play.ahk", "__pycache__", ".git", "BUILD-ZIP-FILE.py"}
files_to_zip = {"hi"}

print("Collected files:")
gitignore_file = folder / ".gitignore"
if gitignore_file.exists():
	with gitignore_file.open() as f:
		spec = pathspec.PathSpec.from_lines("gitwildmatch", f)
else:
	spec = pathspec.PathSpec.from_lines("gitwildmatch", [])

files_to_zip.clear()
for file in folder.rglob("*"):
	if file.is_file() and ".git" not in file.parts and file.name not in custom_exclude and not spec.match_file(str(file.relative_to(folder))):
		print(file.name)
		files_to_zip.add(file.name)

print("\nCopying files...")

folder = Path("build")
folder.mkdir(exist_ok=True)

for file in files_to_zip:
	src = Path(file)
	shutil.copy(src, folder)

print("Zipping...")
zip_file = Path(f"BMCs.Biome.Sniper.{updater.CURRENT}.zip")

with ZipFile(zip_file, "w", compression=ZIP_DEFLATED) as zipf:
	for file in folder.iterdir():
		if file.is_file():
			zipf.write(file, arcname=file.name)