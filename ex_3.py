#!/usr/bin/env python3

data = [4, -30, 100, -100, 123, 1, 0, -1, -4]
# Реализация задания 3
# print (data)
# print(sorted(data, key=lambda x: abs(x)))



#print(sorted(data, key=lambda x: abs(x)))

# print([i for i in data if i > 0])
print(list(filter(lambda x: x>0, data)))
