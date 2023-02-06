a = int(input())
cash = 1000 - a
changes = [500, 100, 50, 10, 5, 1]
count = 0
for i in (changes):
    count += cash//i
    cash %= i
    
print(count)