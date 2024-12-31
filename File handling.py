##'r' means 'read'
# f = open('filedata', 'r')

# print(f.read())

# print(f.readline(), end='')
# print(f.readline())

##'w' means 'write'
# f1 = open('abc', 'w')
# f1.write('something')

# for data in f:
#     f1.write(data)

##'a' means 'append'
# f1 = open('abc', 'a')
# f1.write('Mobile')


##Example2- 'rb' means 'read binary'
f = open('4426473_1.jpg', 'rb')

## 'wb' means 'write binary'
f1 = open('myimg.jpg', 'wb')

for i in f:
    f1.write(i)