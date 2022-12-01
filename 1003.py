a = [1, 0, 1]
b = [0, 1, 1]

def fibonacci(num):
    length = len(a)
    if num >= length:
        for i in range(length, num+1):
            a.append(a[i-1] + a[i-2])
            b.append(b[i-1] + b[i-2])
    print('{} {}'.format(a[num], b[num]))

num = int(input())
    
for i in range(0, num):
    fibonacci(int(input()))