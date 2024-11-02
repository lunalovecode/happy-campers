n, q = [int(x) for x in input().split()]
str = input()
for _ in range(q):
    l, r = [int(x) for x in input().split()]
    sub = str[l - 1:r]
    print(sub.count("AC"))