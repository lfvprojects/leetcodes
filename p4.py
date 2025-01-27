numbers1 = [1,2,3,4]
numbers2 = [3,5,7,8]

result = numbers1 + numbers2
result.sort()
print(result)
resultLength = len(result)
medianIndex = resultLength // 2

if resultLength % 2 == 0:
    median = float((result[medianIndex]+result[medianIndex-1])/2)
else:
    median = int(result[medianIndex])

print("Median:", median)