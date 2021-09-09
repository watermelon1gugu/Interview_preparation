m = {i: 0 for i in range(1, 50)}
for i in range(0, 7):
    for j in range(0, 7):
        m[i*7+j+1] +=1
print(m)
