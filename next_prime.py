def is_prime(n):
    ans = True
    for x in range(2, n):
        if n % x == 0:
            ans = False
    return ans

x = int(input())
found = False
i = x
while found == False:
    if is_prime(i):
        print(i)
        found = True
    i += 1
    