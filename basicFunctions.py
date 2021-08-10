name = open('name.txt')


#text = name.read()
#print(text)


read = name.readlines()
print(read)
for i in read:
    print('hello'+i)