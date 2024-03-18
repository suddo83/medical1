f = open('str.txt','r',encoding='utf8')
while True:
    txt = f.readline()
    if txt.strip() == '': break
    print(txt,end="")
f.close()
print("-"*50)

f = open('str.txt','r',encoding='utf8')
ff = open('str1.txt','a',encoding='utf8')
while True:
    txt = f.readline()
    if txt.strip() == '': break
    print(txt,end="")
    ff.write(txt)
f.close()
ff.close()

fff = open('str1.txt','r',encoding='utf8')
while True:
    txt = fff.readline()
    if txt.strip() == '': break
    print(txt,end="")
fff.close()


