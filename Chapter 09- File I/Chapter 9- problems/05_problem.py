Words = ["Logan", "Kendell", "Shivon"]

with open("file_5.txt", "r") as f:
    content = f.read()

for word in Words:
    content = content.replace(word, "#" * len(word))

with open("file_5.txt", "w") as f:
    f.write(content)        
        
        
