num = [2, 5, 9, 1]
num[2] = 3
num.sort(reverse=True)
num.insert(2, 0)
num.pop(1)
print(num)
print(f'Essa lista tem {len(num)} elementos.')