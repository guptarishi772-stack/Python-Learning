f = open("poem.txt")
content = f.read()
if ("Twinkle" in content):
    print("Word Twinkle is not present")
else:
    print("Word Twinkle is present")
f.close()        

