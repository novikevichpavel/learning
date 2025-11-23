# 1. Создать папку files в текущей папке
# 2. Добавить два файла first.txt и second.txt в эту папку и запишите в них по 2-3 строки текста
# 3. Прочитайте все строки первого файла
# 4. Прочитайте все строки второго файла одну за другой
# 5. Удлаить оба файла и удалить папку files


from pathlib import Path

cwd = Path("files")
cwd.mkdir(exist_ok=True)



with open(cwd / "first.txt", "w") as first_file:
    first_file.write("First line of first file \n")
    first_file.write("Second line of first file \n")
    first_file.write("Third line of first file \n")

with open(cwd / "second.txt", "w") as second_file:
    second_file.write("First line of the second file \n")
    second_file.write("Second line of the second file \n")
    second_file.write("Third line of the second file \n")


with open(cwd / "first.txt") as first_file:
    print(first_file.read())

with open(cwd / "second.txt") as second_file:
    for line in second_file:
        print(line)


Path(cwd / "first.txt").unlink()
Path(cwd / "second.txt").unlink()

cwd.rmdir()
