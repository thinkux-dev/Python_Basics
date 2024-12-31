pos = -1
def search(list, n):
    lowerB = 0
    upperB = len(list)-1

    while lowerB <= upperB:
        mid = (lowerB+upperB) // 2

        if list[mid] == n:
            globals()['pos'] = mid
            return True
        elif list[mid] != n:
            return False
        else:
            if list[mid] < n:
                lowerB = mid
            else:
                upperB = mid

list = [5,8,4,6,9,2]
n = 90

if search(list, n):
    print('Found at:', pos+1)
else:
    print('Not Found')