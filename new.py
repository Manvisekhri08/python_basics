with open("vegetables.txt","a+") as myfile:
    myfile.write("\nMushroom")
    myfile.seek(0)
    content = myfile.read()
print(content)    