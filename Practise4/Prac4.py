import os

# os.makedirs("test")
# os.rmdir("test")
# os.rename("main.py", "run.py")

my_dir = './'
content = os.listdir(my_dir)
print(content)

files = []
for file in content:
    if os.path.isfile(os.path.join(my_dir, file)) and file.endswith(".txt"):
        files.append(file)
print(files)