n = int(input())
result = []

for i in range(n):
    a = int(input())
    result.append(a)
    
result.sort(reverse=True)
re =[]

for i in range(n):
    re.append(result[i]*(i+1))

print(max(re))
    
