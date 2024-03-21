f = open("str.txt","r",encoding="utf8")
while True:
    content = f.readline()
    if content.strip() == "": break 
    print(content,end="")
f.close()
print("-"*50)

f = open("str.txt","r",encoding="utf8")
ff = open("str1.txt","a",encoding="utf8")
while True:
    content = f.readline()  
    if content.strip() == "": break
    ff.write(content)       
f.close()
ff.close()

fff = open("str1.txt","r",encoding="utf8")
while True:
    content = fff.readline()
    if content.strip() == "": break
    print(content,end="")
f = open("str.txt","r",encoding="utf8")
while True:
    content = f.readline()
    if content.strip() == "": break 
    print(content,end="")
f.close()
print("-"*50)

f = open("str.txt","r",encoding="utf8")
ff = open("str1.txt","a",encoding="utf8")
while True:
    content = f.readline()  
    if content.strip() == "": break
    ff.write(content)       
f.close()
ff.close()

fff = open("str1.txt","r",encoding="utf8")
while True:
    content = fff.readline()
    if content.strip() == "": break
    print(content,end="")
fff.close()