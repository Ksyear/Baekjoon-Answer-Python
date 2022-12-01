num = int(input())

for i in range(0, num):
    x1, y1, x2, y2 = list(map(int, input().split()))
    n = int(input())
    count = 0
    for i in range(0, n):
        cx, cy, cr = map(int, input().split())
        d1 = (x1-cx)**2 + (y1-cy)**2
        d2 = (x2-cx)**2 + (y2-cy)**2
        
        if cr**2 > d1 and cr**2 > d2:
            pass
        elif cr**2 > d1:
            count += 1
        elif cr**2 > d2:
            count += 1
            
    print(count)