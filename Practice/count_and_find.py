numbers = [1, 2, 1, 3, 1, 4, 5, 1]
target = 1
count = 0
indices = []
index = 0  

for i in numbers:
    if i == target:
        count += 1
        indices.append(index) 
    index += 1  

print(count)
print(indices)
