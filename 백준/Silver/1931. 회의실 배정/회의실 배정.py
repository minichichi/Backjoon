n = int(input())

time_lists = []
for i in range(n):
    start, end = map(int,input().split(' '))
    time_lists.append([start, end])

time_lists = sorted(time_lists, key = lambda a:a[0] )
time_lists = sorted(time_lists, key = lambda a:a[1] )

last = 0
count = 0

for i, j in time_lists:
    if i >= last:
        count += 1
        last = j

print(count)
