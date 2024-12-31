nums = [12, 16, 18, 20, 25]

for num in nums:
    if num%5==0:
        print(num)
        break
else:
    print('not found')


print('====================================')
#Prime number
num = int(input('Enter number: '))

for i in range(2, num):
    if num % i == 0:
        print('Not Prime')
        break
else:
    print("Prime")