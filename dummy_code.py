def dummy_cubed(n):
    count = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                count +=1
    return count

result = dummy_cubed(5)
print(result)