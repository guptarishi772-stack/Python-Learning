word = "Putin"

with open("file_4.txt", "r") as f:
    content = f.read()
contentNew = content.replace(word, "Hulk") 

with open ("file_4.txt", "w") as f:
    f.write(contentNew)