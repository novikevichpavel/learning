from pathlib import Path
from zipfile import ZipFile

cwd = Path("files")
cwd.mkdir(exist_ok=True)

with open(cwd / "file_one.txt", "w") as first_file:
    first_file.write("This is the first line in this file \n")
    first_file.write("This is the second line in this file \n")

with open(cwd / "file_two.txt", "w") as second_file:
    second_file.write("This is the first line in this file \n")
    second_file.write("This is the first line in this file \n")


with ZipFile("my-files.zip", mode="w") as zipped_file:
    for file in Path("files").iterdir():
        print(zipped_file)
        zipped_file.write(file)


with ZipFile("my-files.zip") as my_file:
    my_file.extractall("my-files-unzipped")

