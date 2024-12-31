
a=5
b=0

try:
    print('resource Open')
    print(a/b)

except ZeroDivisionError as e:
    print('You cannot divide a number by zero: ', e)

except ValueError as e:
    print('Invalid Input')

except Exception as e:
    print('Something went wrong: ', e)

finally:
    print('resource Close')

print('Bye')