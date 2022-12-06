import os

listdir = os.listdir("./")
listdir.remove("normalize.py")
listdir.remove(".git")

for each in listdir:
    if "JPG" in each:
        os.rename(each, each.replace("JPG", "jpg"))

print(listdir)