# i=1;
# while i<=4:
#     print('# ', end='');
#     j=1;
#     while j<=4:
#         print('# ', end='');
#         j=j+1;
#
#     i=i+1;
#     print();

# #================
# for i in range(4):
#     for j in range(i+1):
#         print("# ", end='')
#     print()

#================
for i in range(4):
    for j in range(4-i):
        print("# ", end='')
    print()

# pSqure = [];
# for i in range(1, 501):
#     pSqure.append(i**2);
#     if i in pSqure:
#         print(i)


# # fibonacci 1
# n =50
# a,b = 0, 1
# for i in range(n):
#     print(a, end=' ')
#     a,b = b,a+b

# fibonacci 2
n =50
a,b = 0, 1
while a<= 50:
    print(a, end=' ')
    a,b = b,a+b


# i=5;
# while i>=1:
#     print('# ', end='');
#     j=i;
#     while j>=1:
#         print('# ' );
#         j=j+1;
#     i=i-1;