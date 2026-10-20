n = int(input())
a = []
for i in range(n):
    i = int(input())
    a.append(i)
ch = [x for x in a if x % 2 == 0]
nch = [x for x in a if x % 2 != 0]
print(ch, nch)

