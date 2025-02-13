fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruits.count('apple'))
fruits.reverse()
print(fruits)
fruits.sort()
print(fruits)
print(fruits.index('pear'))
print(fruits.pop())

t1 = 1,2,3
t2 = 4,5,3
print(t1+t2)

s1 = set('abcdefghijk')
s2 = set('fghijklmnopqr')
print(s1-s2) #letters in a but not in b
print(s1|s2) #letters in a or b or both
print(s1&s2) #letter common in both
print(s1^s2) #letters in a or b but not both