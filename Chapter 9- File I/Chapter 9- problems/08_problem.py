with open("this.txt") as f:
    content = f.read()

with open("copythis.txt", "w") as f:
    f.write(content)    