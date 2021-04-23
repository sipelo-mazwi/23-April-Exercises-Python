ages = [2, 12, 12, 14, 15, 16, 16, 17, 18, 14, 20, 20]
print("Largest number is :", ages[-1])

ages2 = []

for i in ages:
    if i not in ages2:
        ages2.append(i)

ages = ages2

print("removed duplicates ", ages)
