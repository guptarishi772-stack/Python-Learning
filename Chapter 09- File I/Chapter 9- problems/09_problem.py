with open("this.txt") as f:
    content1 = f.read()
with open("copythis.txt") as f:
    content2 = f.read()

    if (content1 == content2):
        print("Both files have identical content")
    else:
        print("Both files have different content")         

